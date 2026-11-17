"""Criterion 4: appeals.

For each trial: submit 10 of my own pieces, appeal each one, and check that
the appeal returns under_review, the log gains an appeal entry with my
reasoning, and the original decision entry is unchanged. Then check that an
unknown content_id returns 404.

Usage:
    python appeal_eval.py --label before
"""

import argparse
import json
import os
import time
import uuid
from datetime import datetime

import requests

import audit
import scenarios

BASE_URL = os.environ.get("PG_URL", "http://127.0.0.1:5000")
TRIALS = 3
REASONING = "I wrote this myself. It is from my own messages and coursework."


def decision_entries(content_id):
    """The original decision entries for a content_id (no 'event' key)."""
    return [e for e in audit.entries_for(content_id)
            if e.get("status") == "decided" and "event" not in e]


def appeal_entries(content_id):
    """Entries for a content_id that record an appeal with my reasoning."""
    return [e for e in audit.entries_for(content_id)
            if "event" in e and REASONING in json.dumps(e)]


def run_trial(trial, texts, stamp):
    rows = []
    for i, text in enumerate(texts):
        creator_id = f"appeal_{stamp}_t{trial}_{i}"
        sub = requests.post(f"{BASE_URL}/submit",
                            json={"text": text, "creator_id": creator_id})
        if sub.status_code != 200:
            rows.append({"i": i, "ok": False,
                         "why": f"submit returned {sub.status_code}"})
            continue
        content_id = sub.json()["content_id"]

        before = decision_entries(content_id)
        resp = requests.post(f"{BASE_URL}/appeal",
                             json={"content_id": content_id,
                                   "creator_id": creator_id,
                                   "reasoning": REASONING})
        after = decision_entries(content_id)
        appeals = appeal_entries(content_id)

        body = resp.json() if resp.headers.get("content-type", "").startswith("application/json") else {}
        checks = {
            "under_review": resp.status_code == 200 and body.get("status") == "under_review",
            "appeal_logged": len(appeals) == 1,
            "original_unchanged": len(before) == 1 and before == after,
        }
        failed = [name for name, passed in checks.items() if not passed]
        rows.append({"i": i, "content_id": content_id,
                     "guess": sub.json().get("guess"),
                     "ok": not failed,
                     "why": ", ".join(failed) if failed else ""})

    fake = requests.post(f"{BASE_URL}/appeal",
                         json={"content_id": str(uuid.uuid4()),
                               "creator_id": f"appeal_{stamp}_t{trial}_fake",
                               "reasoning": REASONING})
    return rows, fake.status_code


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", required=True)
    args = parser.parse_args()

    texts = scenarios.SCENARIOS[0]["texts"]
    stamp = datetime.now().strftime("%H%M%S")
    lines = [f"# Appeal run ({args.label}), {datetime.now():%Y-%m-%d %H:%M}", ""]

    for trial in range(1, TRIALS + 1):
        rows, fake_status = run_trial(trial, texts, stamp)
        passed = sum(r["ok"] for r in rows)
        lines.append(f"## Trial {trial}: {passed}/{len(rows)} valid appeals passed, "
                     f"unknown content_id returned {fake_status}")
        lines.append("")
        lines.append("| # | content_id | guess | result |")
        lines.append("|---|---|---|---|")
        for r in rows:
            result = "pass" if r["ok"] else f"FAIL: {r['why']}"
            lines.append(f"| {r['i']} | {r.get('content_id', '')[:8]} | "
                         f"{r.get('guess', '')} | {result} |")
        lines.append("")
        if trial < TRIALS:
            time.sleep(5)

    report = "\n".join(lines)
    print(report)
    os.makedirs("results", exist_ok=True)
    path = f"results/appeals_{datetime.now():%Y-%m-%d_%H%M}_{args.label}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(report + "\n")
    print(f"\nWrote {path}")


if __name__ == "__main__":
    main()