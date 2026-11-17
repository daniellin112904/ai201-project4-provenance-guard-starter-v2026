"""Pull the scores from the latest run_eval.py run out of the audit log.

For each eval_ creator_id, the last 3 decided entries are the 3 trials.
Prints per-piece scores, the criterion 2 gap, the criterion 3 count, and
the criterion 5 rejection check.
"""

from collections import defaultdict
from statistics import mean

import audit

entries = audit.read_entries()
decided = defaultdict(list)
rejected = defaultdict(list)
for e in entries:
    cid = e.get("creator_id") or ""
    if not cid.startswith("eval_"):
        continue
    if e.get("status") == "decided" and "event" not in e:
        decided[cid].append(e)
    elif "reason" in e:
        rejected[cid].append(e)


def scores_for(prefix, n):
    """3 trials x n pieces of combined scores, ordered by piece.
    run_eval.py numbers pieces from 1."""
    table = []
    for i in range(1, n + 1):
        last3 = decided[f"{prefix}_{i}"][-3:]
        table.append([e["combined_score"] for e in last3])
    return table


def show(title, table):
    print(f"\n{title}")
    for i, row in enumerate(table):
        print(f"  piece {i + 1}: " + ", ".join(f"{s:.3f}" for s in row))
    trial_avgs = [mean(row[t] for row in table) for t in range(3)]
    print("  average per trial: " + ", ".join(f"{a:.3f}" for a in trial_avgs))
    return trial_avgs


own = scores_for("eval_my own writi", 10)
casual = scores_for("eval_casual human", 5)
bot = scores_for("eval_chatbot resp", 5)

show("Criterion 1: my own writing", own)
for t in range(3):
    flagged = sum(row[t] >= 0.85 for row in own)
    print(f"  trial {t + 1}: {flagged}/10 at 0.85 or higher")

casual_avg = show("Criterion 2: casual human", casual)
bot_avg = show("Criterion 3: chatbot responses", bot)
for t in range(3):
    reached = sum(row[t] >= 0.85 for row in bot)
    print(f"  trial {t + 1}: {reached}/5 at 0.85 or higher")

print("\nCriterion 2: gap (chatbot average minus casual average)")
for t in range(3):
    gap = bot_avg[t] - casual_avg[t]
    print(f"  trial {t + 1}: {bot_avg[t]:.3f} - {casual_avg[t]:.3f} = {gap:.3f}")

print("\nCriterion 5: bad input")
for cid in sorted(k for k in set(decided) | set(rejected) if k.startswith("eval_bad")):
    print(f"  {cid}: {len(rejected[cid])} rejections logged, "
          f"{len(decided[cid])} decisions (should be 0)")