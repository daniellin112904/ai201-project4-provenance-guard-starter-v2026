"""Raw style features for the chatbot responses vs my casual messages."""

import scenarios
import stylometry

groups = {
    "chatbot": scenarios.SCENARIOS[2]["texts"],
    "casual (mine)": scenarios.SCENARIOS[1]["texts"],
    "formal (mine)": scenarios.SCENARIOS[0]["texts"][:5],
}

print(f"{'group':15} {'#':>2}  {'spread':>6}  {'variety':>7}  {'punct':>5}  {'style':>5}")
for name, texts in groups.items():
    for i, t in enumerate(texts, 1):
        print(f"{name:15} {i:>2}  "
              f"{stylometry.sentence_length_spread(t):6.3f}  "
              f"{stylometry.word_variety(t):7.3f}  "
              f"{stylometry.punctuation_variety(t):5}  "
              f"{stylometry.style_signal(t):5.3f}")