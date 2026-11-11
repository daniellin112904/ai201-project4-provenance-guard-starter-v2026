"""Send the four Milestone 4 test inputs to /submit and print both signals side by side."""
import requests

URL = "http://127.0.0.1:5000/submit"

INPUTS = {
    "clearly AI": (
        "Artificial intelligence has transformed numerous industries by enabling more "
        "efficient processes and data-driven decision making. As organizations continue "
        "to adopt these technologies, it is important to consider both the benefits and "
        "the potential challenges they present."
    ),
    "clearly human": (
        "Bro I completely forgot we had an assignment due tonight. I thought it was due "
        "next week lol. I just got home and haven't even started it yet. Did you finish yours?"
    ),
    "formal human": (
        "One of the biggest challenges I faced during my research project was working with "
        "a limited amount of training data. To address this, I experimented with different "
        "preprocessing techniques and compared the performance of multiple neural network "
        "models. Although some models performed better than others, the results helped me "
        "understand how important data quality is when training machine learning models."
    ),
    "lightly edited AI": (
        "AI has honestly changed a ton of industries. It makes processes way more efficient "
        "and helps people make decisions based on actual data! But as more companies jump on "
        "board, it's worth thinking about both sides: the upsides, sure, and also the real "
        "challenges these tools bring."
    ),
    "AI, punctuation only": (
        "Artificial intelligence has transformed numerous industries. How? By enabling more "
        "efficient processes and data-driven decision making! As organizations continue to "
        "adopt these technologies, it is important to consider both the benefits and the "
        "potential challenges they present: economic, social; and ethical."
    ),
}

print(f"{'input':<20} {'model':>7} {'style':>7} {'gap':>6} {'combined':>9}")
for name, text in INPUTS.items():
    r = requests.post(URL, json={"text": text, "creator_id": "test-m4"}, timeout=60).json()
    gap = abs(r["model_score"] - r["style_score"])
    print(f"{name:<20} {r['model_score']:>7.3f} {r['style_score']:>7.3f} {gap:>6.3f} {r['confidence']:>9.3f}")