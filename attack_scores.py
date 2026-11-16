"""Print one line per attack-run entry from the audit log: compact enough to paste."""
import json

with open("logs/audit.jsonl", encoding="utf-8") as f:
    entries = [json.loads(line) for line in f if line.strip()]

run = [e for e in entries if e.get("timestamp", "") >= "2026-11-16T04:40"]
print(f"{'creator_id':<22} {'status':<10} {'guess':<7} {'model':>6} {'style':>6} {'comb':>6}  reason")
for e in run:
    def fmt(x):
        return f"{x:.3f}" if isinstance(x, (int, float)) else "  -  "
    print(f"{str(e.get('creator_id'))[:22]:<22} {e.get('status',''):<10} {str(e.get('guess') or ''):<7} "
          f"{fmt(e.get('model_score')):>6} {fmt(e.get('style_score')):>6} {fmt(e.get('combined_score')):>6}  {e.get('reason','')}")
print(f"\n{len(run)} entries")