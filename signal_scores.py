import audit

E = [e for e in audit.read_entries()
     if e.get("status") == "decided" and "event" not in e]
ids = [f"eval_chatbot resp_{i}" for i in range(1, 6)]
ids += ["attacker_FP05", "attacker_MF06", "attacker_MF07"]
for c in ids:
    d = [e for e in E if e.get("creator_id") == c]
    if d:
        e = d[-1]
        print(f"{c:22} model {e['model_score']:.3f}  "
              f"style {e['style_score']:.3f}  combined {e['combined_score']:.3f}")