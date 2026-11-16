"""Print the ten audit log entries chosen for the README, as JSON."""
import json

WANTED = ["attacker_FP05", "attacker_MF07", "attacker_MF06", "attacker_FP06",
          "attacker_EV01", "attacker_PI02", "attacker_EV05", "attacker_EV10",
          "attacker_RQ03"]

with open("logs/audit.jsonl", encoding="utf-8") as f:
    run = [json.loads(l) for l in f if l.strip()]
run = [e for e in run if e.get("timestamp", "") >= "2026-11-16T04:40"]

picked = [next(e for e in run if e.get("creator_id") == cid) for cid in WANTED]
picked.append(next(e for e in run if e.get("reason") == "rate_limited"))
print(json.dumps(picked, indent=2, ensure_ascii=False))