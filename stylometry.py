"""
Signal two: the style signal.

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it: adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it.

Each measure becomes a "human-ness" score from 0 to 1, where more variation
means more human. style_signal() averages them and flips the result, so it
points the same way as detector.model_signal: higher means more likely AI.

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough. Given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


def _clamp(x: float) -> float:
    return max(0.0, min(1.0, x))


# ── The three measures ─────────────────────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies, as a coefficient of variation:
    the standard deviation of words per sentence divided by the average.

    Dividing by the average keeps a writer of long sentences from looking
    "more varied" just because their numbers are bigger. Returns 0.0 when
    there are fewer than two sentences, since spread needs at least two.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    return statistics.stdev(lengths) / mean if mean else 0.0


def word_variety(text: str, window: int = 50) -> float:
    """
    Vocabulary variety as a moving-average type-token ratio (MATTR).

    A plain unique-words / total-words ratio falls as text gets longer, since
    every long text repeats common words. Averaging the ratio over sliding
    windows of `window` words removes most of that length effect. Texts
    shorter than one window fall back to the plain ratio.
    """
    w = words(text)
    if not w:
        return 0.0
    if len(w) <= window:
        return len(set(w)) / len(w)
    ratios = [
        len(set(w[i:i + window])) / window
        for i in range(len(w) - window + 1)
    ]
    return statistics.mean(ratios)


PUNCTUATION_MARKS = ["!", "?", ";", ":", "(", '"', "...", "—", " - "]


def punctuation_variety(text: str) -> int:
    """
    How many different kinds of punctuation appear beyond the plain period
    and comma: exclamation and question marks, semicolons, colons,
    parentheses, quotation marks, ellipses, and dashes.

    People punctuate by habit and unevenly; AI writing tends to stick to
    periods and commas.
    """
    return sum(1 for mark in PUNCTUATION_MARKS if mark in text)


# ── Turning the measures into one score ────────────────────────────────────

# Calibration ranges: where each measure goes from "AI-like" (0) to
# "human-like" (1). These are starting guesses, checked in Milestone 4 against
# real AI and human text. Adjust them if a measure barely moves.
SPREAD_RANGE = (0.15, 0.60)      # coefficient of variation
VARIETY_RANGE = (0.60, 0.90)     # moving-average type-token ratio
PUNCTUATION_FULL = 3             # this many kinds of mark counts as fully human


def _scaled(value: float, low: float, high: float) -> float:
    return _clamp((value - low) / (high - low))


def style_measures(text: str) -> dict:
    """Each raw measure and its 0 to 1 human-ness score, for printing and debugging."""
    spread = sentence_length_spread(text)
    variety = word_variety(text)
    punct = punctuation_variety(text)

    # One sentence gives no spread information, so that measure stays neutral.
    spread_h = 0.5 if len(sentences(text)) < 2 else _scaled(spread, *SPREAD_RANGE)

    return {
        "sentence_length_spread": round(spread, 4),
        "word_variety": round(variety, 4),
        "punctuation_variety": punct,
        "spread_humanness": round(spread_h, 4),
        "variety_humanness": round(_scaled(variety, *VARIETY_RANGE), 4),
        "punctuation_humanness": round(_clamp(punct / PUNCTUATION_FULL), 4),
    }


def style_signal(text: str) -> float:
    """
    One 0 to 1 score from the three measures. Higher means more likely AI,
    matching detector.model_signal.

    The three human-ness scores are averaged with equal weight, then flipped.
    """
    m = style_measures(text)
    humanness = (
        m["spread_humanness"]
        + m["variety_humanness"]
        + m["punctuation_humanness"]
    ) / 3
    return round(1.0 - humanness, 4)


if __name__ == "__main__":
    import sys

    sample = " ".join(sys.argv[1:]) or (
        "The results were clear. However, further research is needed to "
        "confirm these findings. Additional studies should examine the "
        "underlying mechanisms in more detail."
    )
    for name, value in style_measures(sample).items():
        print(f"{name:<24} {value}")
    print(f"{'style_signal':<24} {style_signal(sample)}   (higher = more likely AI)")