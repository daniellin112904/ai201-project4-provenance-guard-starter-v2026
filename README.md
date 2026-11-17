# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

Provenance Guard is a small backend service a writing site could plug in. Text comes in; back comes a guess about whether it was AI-generated, a confidence score, a plain-English label for the writer, and a way to appeal.

### The path a submission takes

1. **Request arrives** at `POST /submit` with `text` and `creator_id`.
2. **Input check:** missing or empty `text` or `creator_id` is rejected with a 400.
3. **Signal one** (`detector.py`): GPT-2 measures how predictable the text is, giving `model_score` from 0 to 1.
4. **Signal two** (`stylometry.py`): measures the text's shape (sentence length spread, word variety, punctuation), giving `style_score` from 0 to 1.
5. **Combine** (`scoring.py::combine_signals`): the two scores become one `combined_score`.
6. **Label** (`scoring.py::score_to_label`): the score maps to `ai`, `human`, or `unsure`, plus the sentence the writer sees.
7. **Log and respond:** `audit.log_decision` writes the entry to `logs/audit.jsonl`, and the response returns the `content_id`, guess, score, and label.

The writer can then send that `content_id` to `POST /appeal`, which records their reasoning and moves the item to `under_review`.

### Tracing a false positive

A student writes a formal essay entirely by themselves: standard five-paragraph structure, careful grammar, consistent sentence lengths. Both signals fail in the same direction. GPT-2 finds the language predictable, so signal one scores high, perhaps 0.7 to 0.8. The consistent sentences and tidy punctuation push signal two high too, perhaps 0.6 to 0.8. These are guesses, not measured results. Combined, the essay could land around 0.7.

Because neither signal disagrees, combining them doesn't protect this writer. The only protection is the threshold. A wrong accusation costs a real writer far more than a missed piece of AI text costs the site, so I want a score of 0.7 to read as **unsure**, not AI. I'll set the high-confidence AI threshold around 0.85, knowing that means a lot of genuinely AI-written text will also land in "unsure." Even at the top of the range, the label should read as an estimate, not proof.

If they're still labeled wrongly, the writer can appeal with their `content_id` and an explanation. The appeal is recorded beside the original decision and the item moves to `under_review` for a person to look at; nothing is re-scored automatically.

### Endpoints

**`POST /submit`**

| In           | Type   | Notes               |
| ------------ | ------ | ------------------- |
| `text`       | string | Required, not empty |
| `creator_id` | string | Required            |

| Out                          | Type   | Notes                                               |
| ---------------------------- | ------ | --------------------------------------------------- |
| `content_id`                 | string | New unique ID, used to appeal                       |
| `guess`                      | string | `"ai"`, `"human"`, or `"unsure"`                    |
| `confidence`                 | float  | Combined score, 0 to 1, higher means more likely AI |
| `label`                      | string | The sentence the writer sees                        |
| `model_score`, `style_score` | float  | Each signal's own score                             |
| `status`                     | string | `"decided"`                                         |

Missing or empty `text` or `creator_id` returns 400 with an `error` message.

**`POST /appeal`**

| In           | Type   | Notes                              |
| ------------ | ------ | ---------------------------------- |
| `content_id` | string | Required, must exist               |
| `reasoning`  | string | Required, the writer's explanation |

| Out          | Type   | Notes                                |
| ------------ | ------ | ------------------------------------ |
| `content_id` | string | Echoed back                          |
| `status`     | string | `"under_review"`                     |
| `message`    | string | Confirmation the appeal was recorded |

Missing fields return 400; an unknown `content_id` returns 404.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to GPT-2, a small language model running locally. `detector.py` computes perplexity, how surprised GPT-2 is by each next word, and turns low perplexity into a high `model_score`.

**Why that might differ between human and AI writing:** Language models generate text by picking likely next words, so AI writing tends to be smooth and predictable. People make less expected word choices, change direction mid-thought, and use specific details a model wouldn't guess.

**What it can't see:** Predictable doesn't mean machine-written. Formal or formulaic human writing scores as AI: academic essays that follow the standard structure, professional emails full of stock phrases, technical instructions, and simple writing with basic vocabulary and short sentences, including from people writing in a second language. Very short texts give it too little to go on. In the other direction, AI text that's been edited to be less predictable (mixed sentence lengths, slang, unusual words, personal details, deliberate typos) can raise perplexity enough to pass as human.

### Signal two — the style signal

**What it measures:** The shape of the text, not its meaning. Three features combined into one `style_score`: how much sentence lengths vary, how varied the vocabulary is (unique words divided by total words), and how punctuation is used. More variation on each points toward human.

**Why that might differ between human and AI writing:** People tend to mix short and long sentences, reach for less common words, and use punctuation unevenly according to habit. AI writing often settles into consistent sentence lengths, reuses similar phrasing, and punctuates uniformly.

**What it can't see:** It only sees patterns, never who wrote the text or what it means. A careful human writing a formal essay produces consistent sentences and tidy punctuation and looks machine-like, while AI text edited to vary sentence length or add punctuation looks human. Word variety also depends on length: longer texts naturally repeat more words, so a long human piece can look less varied than a short AI one for reasons that have nothing to do with authorship. These are tendencies, not rules.

### The combining rule

**The rule:** A weighted average that leans on the style signal, plus a disagreement rule. If the two signals differ by more than 0.3, they disagree, and the combined score is set to 0.5, inside the unsure band, no matter which way the average would have leaned. Two methods disagreeing is uncertainty, so a sharp disagreement can produce neither a confident AI label nor a confident human label. I would rather the system admit it isn't sure than confidently give the wrong label in either direction.

I weighted the style signal more heavily because, on my test inputs, the model signal scored my own formal research writing (0.844) higher than real AI text (0.784), while the style signal scored it lower (0.693). Leaning on the style signal reduces the pull toward accusing formal human writers. The cost is that real AI text scores lower too.

**The numbers:** (all in `config.py`)

| Setting               | Value |
| --------------------- | ----- |
| `WEIGHT_MODEL_SIGNAL` | 0.3   |
| `WEIGHT_STYLE_SIGNAL` | 0.7   |
| `DISAGREEMENT_GAP`    | 0.3   |
| `DISAGREEMENT_SCORE`  | 0.5   |
| `AI_THRESHOLD`        | 0.85  |

**Where it lives:** `scoring.py::combine_signals`

**The test inputs** (from `test_inputs.py`, run against the live `/submit` route):

| Input                                   | Model | Style | Gap   | Combined |
| --------------------------------------- | ----- | ----- | ----- | -------- |
| Clearly AI (unedited chatbot paragraph) | 0.784 | 0.636 | 0.147 | 0.680    |
| Clearly human (my casual message)       | 0.518 | 0.433 | 0.085 | 0.458    |
| Formal human (my research writing)      | 0.844 | 0.693 | 0.151 | 0.738    |
| Lightly edited AI (casual rewrite)      | 0.359 | 0.176 | 0.183 | 0.231    |
| AI, punctuation only (same words)       | 0.642 | 0.000 | 0.642 | 0.500    |

**A case where my two signals split, and what my rule does with it:** The "AI, punctuation only" input keeps the clearly-AI paragraph's exact words but changes only its punctuation and sentence breaks: one sentence split in two, a question, an exclamation mark, a colon and a semicolon. The model signal, which reads word choice, still found it fairly predictable at 0.642. The style signal, which reads shape, saw varied sentences and varied punctuation and scored it 0.000, fully human. A plain 30/70 average gave 0.193, which would have read as a confident human label for text that is entirely AI, produced by a ten-second trick. My first version of the rule only capped disagreements on the way up, to protect writers from accusations, so it missed this. I made it symmetric: a gap of 0.642 is well past 0.3, so the score is set to 0.5 and the label is "unsure".

**What the rule can't fix:** It only helps when the signals disagree. When both are fooled the same way, there's nothing for it to catch. My formal research writing still scores above real AI text, because both signals read formal writing as machine-like. And the lightly edited AI text scores 0.231, lower than my genuine casual message, because a casual rewrite raised the model signal's perplexity and changed the shape the style signal reads at the same time. I also found that word variety barely discriminates on short texts: all my inputs scored between 0.88 and 0.92, and the AI paragraph had the most varied vocabulary, the opposite of what I expected.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label                 | Score range     | The exact text a reader sees                                                                                                                                                                                            |
| --------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| high-confidence human | below 0.20      | "This writing appears to have been written by a person, with little indication of AI involvement. However, this result is not a guarantee."                                                                             |
| unsure                | 0.20 up to 0.85 | "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision." |
| high-confidence AI    | 0.85 and above  | "This writing shows strong signs of being AI-generated. However, this is only an estimate and does not necessarily mean AI was used. If you believe this result is incorrect, you can submit an appeal."                |

The thresholds live in `config.py` (`HUMAN_THRESHOLD = 0.20`, `AI_THRESHOLD = 0.85`) and the label text in `scoring.py::score_to_label`. All three are reachable. From `test_inputs.py`: a very casual message full of slang and mixed punctuation scored 0.125 (human), a deliberately repetitive paragraph scored 0.994 (AI), and everything else, including real AI text and my own normal writing, landed in unsure. Each confident label takes fairly extreme text to reach, which is the design: a confident label in either direction has to be earned.

**Why I worded the "unsure" one this way:** Most genuine writers will see this label. My own casual message (0.458) and my own research writing (0.738) both land here. So it's written for someone who wrote every word themselves. It says plainly that it is not an accusation ("This does not mean your writing is AI-generated") and puts the uncertainty on the system, not the writer ("our system doesn't have enough evidence"). I avoided anything that sounds like a warning or a partial verdict, because a reader who sees "we couldn't tell" next to their own work will otherwise assume the worst.

<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

---

## Sample Run

**A submission**

```
$ curl.exe -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d '{\"text\": \"One of the biggest challenges I faced during my research project was working with a limited amount of training data. To address this, I experimented with different preprocessing techniques and compared the performance of multiple neural network models.\", \"creator_id\": \"daniel\"}'
```

```json
{
  "confidence": 0.7369,
  "content_id": "fa6ba504-baf9-493f-8f87-687b983402f8",
  "guess": "unsure",
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "model_score": 0.8189,
  "status": "decided",
  "style_score": 0.7018
}
```

This is my own writing. Both signals read it as fairly machine-like, but at 0.737 it stays under the 0.85 AI threshold, so it gets "unsure" rather than an accusation.

**An appeal**

```
$ curl.exe -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d '{\"content_id\": \"fa6ba504-baf9-493f-8f87-687b983402f8\", \"reasoning\": \"I wrote this myself for my research project write-up.\"}'
```

```json
{
  "content_id": "fa6ba504-baf9-493f-8f87-687b983402f8",
  "message": "Your appeal has been recorded. A person will review this decision.",
  "status": "under_review"
}
```

An appeal on a `content_id` that doesn't exist returns 404:

```
$ curl.exe -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d '{\"content_id\": \"does-not-exist\", \"reasoning\": \"test\"}'
```

```json
{
  "error": "not_found",
  "message": "No submission found with content_id does-not-exist"
}
```

**What the log shows afterwards**

```
$ curl.exe "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": 0.9942,
      "content_id": "ec2b7e02-14d5-4f9e-bfd3-625de154e080",
      "creator_id": "test-m4",
      "guess": "ai",
      "label": "This writing shows strong signs of being AI-generated. However, this is only an estimate and does not necessarily mean AI was used. If you believe this result is incorrect, you can submit an appeal.",
      "model_score": 0.9808,
      "status": "decided",
      "style_score": 1.0,
      "timestamp": "2026-11-11T05:31:38+00:00"
    },
    {
      "combined_score": 0.7369,
      "content_id": "fa6ba504-baf9-493f-8f87-687b983402f8",
      "creator_id": "daniel",
      "guess": "unsure",
      "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
      "model_score": 0.8189,
      "status": "decided",
      "style_score": 0.7018,
      "timestamp": "2026-11-11T05:34:15+00:00"
    },
    {
      "content_id": "fa6ba504-baf9-493f-8f87-687b983402f8",
      "creator_id": "daniel",
      "event": "appeal",
      "reasoning": "I wrote this myself for my research project write-up.",
      "status": "under_review",
      "timestamp": "2026-11-11T05:35:59+00:00"
    }
  ]
}
```

The original decision for `fa6ba504...` is still in the log exactly as it was, and the appeal sits after it with the writer's reasoning and the new `under_review` status. The log is append-only, so the order shows what was decided and when it was challenged.

---

## How I Used AI

**Moment 1**

- _What I asked for:_ Help turning my three style features (sentence length spread, word variety, punctuation) into working code in `stylometry.py`.
- _What came back:_ Claude wrote the three measures and `style_signal`, including a moving-average type-token ratio to deal with the length problem I'd named in my blind spot, and calibration ranges it marked as guesses to check. When I ran it on my three test texts, word variety scored between 0.88 and 0.92 for all of them, so it barely discriminated, and the AI paragraph had the most varied vocabulary of the three, the opposite of my hypothesis.
- _What I changed:_ I didn't tune the ranges to make three samples come out the way I wanted. I kept the measure, recorded that it doesn't discriminate on short texts as a finding, and leaned on the evidence that sentence length spread was the feature actually separating casual writing from formal writing.

**Moment 2**

- _What I asked for:_ Help testing my combining rule and choosing the human threshold.
- _What came back:_ Claude suggested building an input that would split the two signals: the AI paragraph with its exact words but only the punctuation changed. It scored 0.642 on the model signal and 0.000 on the style signal, and my first rule, which only capped disagreements on the way up, let it through at 0.193, a confident human label for AI text. Later, when we discussed the human threshold, Claude used 0.25 as an example of a stricter setting.
- _What I changed:_ I decided the disagreement rule had to be symmetric, so any gap over 0.3 sets the score to 0.5 and the label to unsure in either direction. For the threshold, I noticed that 0.25 wouldn't actually stop my lightly edited AI text, which scored 0.231, so I set the human threshold to 0.20 instead.

**Who wrote what:** I made the design decisions: both signals' features and directions, the 30/70 weighting, the symmetric disagreement rule, both thresholds, all five criteria, and the label wording. Claude wrote most of the code to implement them (`stylometry.py`, the `/submit` and `/appeal` routes, and `test_inputs.py`), explained test results, and checked whether each criterion could be verified by someone else.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 8 per minute, 100 per day, on `POST /submit` (`config.py`: `RATE_LIMIT_PER_MINUTE`, `RATE_LIMIT_PER_DAY`).

**Why those numbers and not others:** A real writer submits their own work a few times an hour, and might resubmit several times in a row while revising a draft. 8 a minute leaves room for a burst of revisions without blocking them. 100 a day is far more than a writer needs, but stops a script sending thousands of variations to map where my 0.20 and 0.85 thresholds sit. These limits slow probing rather than prevent it: a careful script doesn't need thousands of tries, since a binary search can locate a threshold in roughly 10 to 20 well-chosen submissions, which fits inside 100 a day. The per-minute limit mostly forces an attacker to be patient.

**What a caller counts as:** The `creator_id` in the request, falling back to the caller's address when there isn't a usable one. This is what the starter's `rate_limit_key` in `app.py` does. The weakness is that `creator_id` is whatever the caller sends: a script that changes it on every request looks like a thousand different writers and is never limited. Per-address limiting fails the other way, since a whole household or school network behind one address would share one budget.

**The run of status codes when I pushed past it:**

```
$ python run_attacks.py --flood 15
15 submissions as 'flood_tester' against http://127.0.0.1:5000

200 200 200 200 200 200 200 200 429 429 429 429 429 429 429

7 of 15 were rate limited.
```

The first 8 succeed and every request after that in the same minute gets a 429. Each rejection is written to the audit log by the starter's 429 handler, and inputs my own route refuses (missing, empty, non-string or oversized text, or a missing `creator_id`) are logged as rejections by `submit()` with `audit.log_rejection`.

---

## Attack Run — Before

`python run_attacks.py --set attack_set --label before`, written to `results/attack_run_2026-11-15_2340_before.md`. Scores below are from the audit log for the same run.

**How I marked each one:** an attack **broke** if it got what its `targets` column was going for: AI text labeled human (evasion, prompt injection), human writing labeled AI (false positive), or a crash, a 500, or a confident verdict on text that isn't writing (malformed). An attack that ended in "unsure" or a clean 400 **held**.

| ID                 | Family            | Going for                                                                       | Status       | Guess  | Combined  | Mark                                              |
| ------------------ | ----------------- | ------------------------------------------------------------------------------- | ------------ | ------ | --------- | ------------------------------------------------- |
| EV01               | evasion           | typos raise word variety                                                        | 200          | unsure | 0.500     | held (disagreement rule)                          |
| EV02               | evasion           | broken-up sentences                                                             | 200          | unsure | 0.500     | held (disagreement rule)                          |
| EV03               | evasion           | pasted quotation                                                                | 200          | unsure | 0.500     | held (disagreement rule)                          |
| EV04               | evasion           | unusual words raise perplexity                                                  | 200          | unsure | 0.638     | held                                              |
| EV05               | evasion           | heavy human editing pass                                                        | 200          | unsure | 0.283     | held                                              |
| EV06               | evasion           | one very long, one very short sentence                                          | 200          | unsure | 0.445     | held                                              |
| EV07               | evasion           | padding with punctuation                                                        | 200          | unsure | 0.413     | held                                              |
| EV08               | evasion           | text below the token window                                                     | 200          | unsure | 0.500     | held (disagreement rule)                          |
| EV09               | evasion           | human opening bolted on                                                         | 200          | unsure | 0.513     | held                                              |
| EV10               | evasion           | repeated stanza structure                                                       | 200          | ai     | 0.867     | held (caught)                                     |
| FP01               | false positive    | plain human writing                                                             | 200          | unsure | 0.565     | held                                              |
| FP02               | false positive    | formal register                                                                 | 200          | unsure | 0.743     | held                                              |
| FP03               | false positive    | non-native English speaker                                                      | 200          | unsure | 0.678     | held                                              |
| FP04               | false positive    | student essay to a rubric                                                       | 200          | unsure | 0.666     | held                                              |
| **FP05**           | false positive    | technical documentation by a person                                             | 200          | **ai** | **0.854** | **broke**                                         |
| FP06               | false positive    | formal letter template                                                          | 200          | unsure | 0.500     | held (disagreement rule)                          |
| FP07               | false positive    | deliberate repetition                                                           | 200          | unsure | 0.731     | held                                              |
| FP08               | false positive    | very short human submission                                                     | 200          | unsure | 0.417     | held                                              |
| PI01               | prompt injection  | instruction to ignore the check                                                 | 200          | unsure | 0.372     | held                                              |
| PI02               | prompt injection  | fake system message                                                             | 200          | unsure | 0.217     | held (0.017 above the human line)                 |
| PI03               | prompt injection  | instruction in the writer's voice                                               | 200          | unsure | 0.389     | held                                              |
| PI04               | prompt injection  | hostile label text                                                              | 200          | unsure | 0.442     | held (label text is fixed, input is never echoed) |
| PI05               | prompt injection  | inject fields into the audit log                                                | 200          | unsure | 0.500     | held (log entry escaped, still valid JSON)        |
| PI06               | prompt injection  | instruction plus real human text                                                | 200          | unsure | 0.549     | held                                              |
| MF01               | malformed         | whitespace only                                                                 | 400          |        |           | held                                              |
| **MF02**           | malformed         | single character                                                                | **500**      |        |           | **broke** (crash, no log entry)                   |
| MF03               | malformed         | control characters                                                              | 200          | unsure | 0.500     | held                                              |
| MF04               | malformed         | punctuation only                                                                | 200          | unsure | 0.500     | held                                              |
| MF05               | malformed         | one very long word                                                              | 200          | unsure | 0.500     | held                                              |
| **MF06**           | malformed         | emoji only                                                                      | 200          | **ai** | **0.882** | **broke**                                         |
| **MF07**           | malformed         | right-to-left script (Arabic)                                                   | 200          | **ai** | **0.855** | **broke**                                         |
| MF08               | malformed         | 60,000 characters                                                               | 400          |        |           | held                                              |
| RQ01 to RQ12       | malformed request | missing fields, wrong types, arrays, bad JSON, wrong content type, deep nesting | 400 (all 12) |        |           | held                                              |
| FL01_01 to FL01_08 | flood             | rate limit fails                                                                | 200          | unsure | 0.500     | held                                              |
| FL01_09 to FL01_12 | flood             | rate limit fails                                                                | 429          |        |           | held                                              |

**Count: 52 held, 4 broke** (FP05, MF02, MF06, MF07).

The evasion results need one caveat: my unedited AI paragraph already scored 0.680 last unit, so AI text rarely reaches the AI label in the first place. The evasions "held" partly because there was little to evade. The closest ones were EV05 (0.283) and PI02 (0.217), both a few hundredths above the 0.20 human threshold. PI02 got there not because anything read its instruction, but because its unusual tokens raised GPT-2's perplexity, so it behaved like an evasion.

The disagreement rule fired on 13 rows. It caught three evasions (EV01, EV02, EV03) and also protected a human: FP06 had a model score of 0.881, and without the rule a 0.3/0.7 average would have given 0.652, but its gap of 0.328 sent it to 0.500.

**Ten audit log entries from the run** (`results/ten_entries.json`, picked by `pick_entries.py`): the three wrong AI labels (FP05, MF07, MF06), the disagreement rule protecting a human (FP06) and catching an evasion (EV01), the two closest evasions (PI02, EV05), the one AI text that was caught (EV10), a 400 rejection from my route (RQ03), and a 429 rejection from the flood rows. MF02 has no entry, because the crash happened before anything was logged.

```json
[
  {
    "timestamp": "2026-11-16T04:40:03+00:00",
    "content_id": "269d27a3-f4dd-42f5-9503-e166ee2d8acf",
    "creator_id": "attacker_FP05",
    "guess": "ai",
    "model_score": 0.8005,
    "style_score": 0.8774,
    "combined_score": 0.8543,
    "label": "This writing shows strong signs of being AI-generated. However, this is only an estimate and does not necessarily mean AI was used. If you believe this result is incorrect, you can submit an appeal.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-16T04:40:06+00:00",
    "content_id": "045d61c9-fbf9-4f64-8c0c-411969dfdf81",
    "creator_id": "attacker_MF07",
    "guess": "ai",
    "model_score": 0.9064,
    "style_score": 0.8333,
    "combined_score": 0.8552,
    "label": "This writing shows strong signs of being AI-generated. However, this is only an estimate and does not necessarily mean AI was used. If you believe this result is incorrect, you can submit an appeal.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-16T04:40:06+00:00",
    "content_id": "39d0d746-a179-4abb-b52f-7d77b1131c7a",
    "creator_id": "attacker_MF06",
    "guess": "ai",
    "model_score": 0.9969,
    "style_score": 0.8333,
    "combined_score": 0.8824,
    "label": "This writing shows strong signs of being AI-generated. However, this is only an estimate and does not necessarily mean AI was used. If you believe this result is incorrect, you can submit an appeal.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-16T04:40:03+00:00",
    "content_id": "5c2d3612-17b2-4c42-a12b-356ba5fe225c",
    "creator_id": "attacker_FP06",
    "guess": "unsure",
    "model_score": 0.8814,
    "style_score": 0.5532,
    "combined_score": 0.5,
    "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-16T04:40:01+00:00",
    "content_id": "2f03fa6c-1339-46db-ada7-db6a9e479b36",
    "creator_id": "attacker_EV01",
    "guess": "unsure",
    "model_score": 0.1635,
    "style_score": 0.6587,
    "combined_score": 0.5,
    "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-16T04:40:04+00:00",
    "content_id": "1063767e-d8ad-4a7e-ae15-461ca97677a6",
    "creator_id": "attacker_PI02",
    "guess": "unsure",
    "model_score": 0.2044,
    "style_score": 0.2222,
    "combined_score": 0.2169,
    "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-16T04:40:02+00:00",
    "content_id": "088ef66b-cf60-4923-9179-916111f4fa2c",
    "creator_id": "attacker_EV05",
    "guess": "unsure",
    "model_score": 0.3212,
    "style_score": 0.2674,
    "combined_score": 0.2835,
    "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-16T04:40:03+00:00",
    "content_id": "f0c919b9-2e1a-4453-8404-432671ae29dc",
    "creator_id": "attacker_EV10",
    "guess": "ai",
    "model_score": 0.9792,
    "style_score": 0.8193,
    "combined_score": 0.8673,
    "label": "This writing shows strong signs of being AI-generated. However, this is only an estimate and does not necessarily mean AI was used. If you believe this result is incorrect, you can submit an appeal.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-16T04:40:06+00:00",
    "creator_id": "attacker_RQ03",
    "event": "rejected",
    "status": "rejected",
    "reason": "text must be a string"
  },
  {
    "timestamp": "2026-11-16T04:40:06+00:00",
    "creator_id": "attacker_flood",
    "event": "rejected",
    "status": "rejected",
    "reason": "rate_limited",
    "limit": "8 per 1 minute"
  }
]
```

**The single worst outcome** — the one I'd least want to explain to a writer whose work got caught by it: **MF07.** A sentence in Arabic got the high-confidence AI label, combined score 0.855. The writer is told their work shows strong signs of being AI-generated purely because my style signal cannot read their alphabet. `stylometry.words()` only matches `[a-z0-9']`, so it finds no words in Arabic text and falls back to a style score of 0.833, and GPT-2, an English model, also found it very predictable. FP05 is also a wrong accusation, but there the system at least measured the text and misjudged it. With MF07 it made a confident accusation from features it could not measure at all, and it would do the same to every writer working in a non-Latin script. For text it can't analyze, it should say "unsure", not "AI".

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

**What I tested with** (`scenarios.py`):

- **Criterion 1:** 10 pieces of my own writing. The first 5 are formal: an email I sent the CS department asking to enroll in a course, and four written answers I gave during my AI201 projects. The last 5 are casual messages I typed in other chats. I left my typos in. The only edit was removing my student ID from the email.
- **Criterion 2:** the same 5 casual messages.
- **Criterion 3:** 5 unedited chatbot responses, written by Claude for this test, as plain paragraphs on everyday topics.
- **Criterion 5:** the 10 bad bodies my criterion names: missing text, null, empty, whitespace only, a number, a list, an object, missing `creator_id`, empty `creator_id`, and 10,005 characters.

`run_eval.py` can't test appeals, since an appeal needs a real `content_id`, so I wrote `appeal_eval.py` for criterion 4. `run_eval.py` also only prints labels, so `eval_scores.py` reads the scores for criteria 1 to 3 from the audit log with `audit.read_entries()`.

```
python appeal_eval.py --label before   ->  results/appeals_2026-11-16_2344_before.md
python run_eval.py --label before      ->  results/run_2026-11-16_2346_before.md
python eval_scores.py
```

| Criterion                        | Target                                              | Run 1                   | Run 2                   | Run 3                   | Verdict             |
| -------------------------------- | --------------------------------------------------- | ----------------------- | ----------------------- | ----------------------- | ------------------- |
| 1. False positives on my writing | At most 1 of 10 at 0.85+                            | 0 of 10 (highest 0.610) | 0 of 10 (highest 0.610) | 0 of 10 (highest 0.610) | **Holds**           |
| 2. Score spread                  | Chatbot average at least 0.40 above casual          | 0.696 - 0.294 = 0.402   | 0.402                   | 0.402                   | **Holds, by 0.002** |
| 3. AI text reaches the AI label  | At least 4 of 5 at 0.85+                            | 0 of 5 (highest 0.746)  | 0 of 5                  | 0 of 5                  | **Misses**          |
| 4. Appeals                       | 10 of 10 valid appeals work, unknown id returns 404 | 10 of 10, 404           | 10 of 10, 404           | 10 of 10, 404           | **Holds**           |
| 5. Bad input                     | 10 of 10 return 400 with no decision                | 10 of 10                | 10 of 10                | 10 of 10                | **Holds**           |

1. **Holds.** `scoring.py::score_to_label` only gives `ai` at 0.85 or higher, and none of my pieces got close. My formal pieces scored higher than my casual ones (0.500 to 0.610 vs 0.182 to 0.370), the pattern I expected, but never near the threshold. Nine came back `unsure` and one `human`. Two landed at exactly 0.500, where the disagreement rule in `combine_signals` fired.
2. **Holds by 0.002.** That's stable across trials but not robust. Swapping one casual piece could push it under 0.40.
3. **Misses.** All five chatbot responses scored 0.664 to 0.746 and came back `unsure`.
4. **Holds.** The `/appeal` route in `app.py` returned `under_review` 30 of 30 times. Each one added a new entry through `audit.log_appeal` with my reasoning, and the original decision entry was unchanged. A made up `content_id` returned 404 every trial.
5. **Holds.** The validation in `app.py::submit` rejected all 10 bodies every trial: 30 rejections logged through `audit.log_rejection`, zero decisions. The two bodies with no usable `creator_id` are logged under `'unknown'` and `''`.

**The three trials are identical** because GPT-2 and stylometry are deterministic, so the same text always gets the same score. The trials show the results are stable, not that they'd hold on different samples.

**Real output from one trial**, pasted as text, naming the file and function that produced it:

Labels, from `run_eval.py` (trial 1):

```
my own writing  (criterion 1)
  trial 1: unsure, unsure, unsure, unsure, unsure, unsure, unsure, human, unsure, unsure
casual human  (criterion 2)
  trial 1: unsure, unsure, human, unsure, unsure
chatbot responses  (criterion 3)
  trial 1: unsure, unsure, unsure, unsure, unsure
bad input  (criterion 5)
  trial 1: no decision on all 10
```

Scores, from `eval_scores.py` reading `audit.read_entries()` (trial 1 column):

```
Criterion 1: my own writing
  pieces 1 to 10: 0.500, 0.503, 0.527, 0.610, 0.500, 0.289, 0.370, 0.182, 0.360, 0.268
  0/10 at 0.85 or higher

Criterion 2: casual human average 0.294
Criterion 3: chatbot responses
  pieces 1 to 5: 0.677, 0.684, 0.664, 0.710, 0.746
  average 0.696, 0/5 at 0.85 or higher
Criterion 2 gap: 0.696 - 0.294 = 0.402

Criterion 5: each eval_bad_ id has 3 rejections logged, 0 decisions
```

Appeals, from `appeal_eval.py::run_trial` (trial 1):

```
## Trial 1: 10/10 valid appeals passed, unknown content_id returned 404
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

**The pattern: two problems, not five.** Four of the five failures trace to signal two, `stylometry.py::style_signal`, which carries 0.7 of the weight in `combine_signals`. It misreads in both directions: it calls chatbot text half human, and it calls uniform or unreadable text AI. The fifth failure is in the route.

| Failure                    | Stage                                | Model          | Style          | Gap          |
| -------------------------- | ------------------------------------ | -------------- | -------------- | ------------ |
| Criterion 3 (chatbot text) | Signal two, amplified by the weights | 0.819 to 0.903 | 0.578 to 0.697 | 0.20 to 0.29 |
| FP05 (technical docs)      | Signal two                           | 0.800          | 0.877          | 0.077        |
| MF06 (emoji)               | Signal two, and the route            | 0.997          | 0.833          | 0.164        |
| MF07 (Arabic)              | Signal two, and the route            | 0.906          | 0.833          | 0.073        |
| MF02 (one character)       | The route                            | none           | none           | none         |

**Criterion 3 missed: chatbot text never reaches the AI label.** Signal one did its job and scored all five chatbot responses between 0.819 and 0.903. Signal two scored them only 0.578 to 0.697. I broke signal two into its three features (`feature_breakdown.py`): sentence length spread and punctuation correctly read the chatbot text as machine-like (four of the five used no varied punctuation at all), but word variety read it as very human. Word variety ranged from 0.771 to 0.895 for the chatbot text and 0.785 to 0.915 for my casual messages, so it doesn't separate the two at all, but it still counts for a third of signal two. That pulled signal two toward the middle, and because signal two carries 0.7 of the weight, it pulled every combined score down to between 0.664 and 0.746. The gaps were 0.20 to 0.29, just under the 0.3 disagreement line, so that rule never fired. This is partly the cost I chose in Unit 7: I leaned on signal two to protect formal human writers, and that also protects chatbot text. It's also the same word variety problem I found in Unit 7, where every input scored between 0.88 and 0.92.

**FP05: human technical documentation labeled AI (0.854).** Both signals scored it high (0.800 and 0.877) with a gap of only 0.077, so the disagreement rule had nothing to catch. Technical writing is meant to be consistent, and consistency is exactly what signal two reads as machine-like. At 0.7 weight, its 0.877 put the score 0.004 over the 0.85 line. This is the blind spot I named for signal two in Unit 7: it can't tell a careful human from a machine.

**MF06 and MF07: emoji and Arabic labeled AI (0.882 and 0.855). One cause.** Both got a style score of exactly 0.833. `stylometry.words()` only matches `[a-z0-9']`, so it finds zero words in emoji or Arabic text. Word variety and punctuation both come out as 0 humanness, sentence spread falls back to a neutral 0.5, and (0.5 + 0 + 0) / 3 = 0.167 humanness gives a style score of 0.833. Signal two can't measure this text, and it reports "can't measure" as "looks like AI." Signal one is an English model, and it was also confident on both (0.997 and 0.906), so the signals agreed and the disagreement rule couldn't step in. The route also never checks whether the text has anything signal two can read before scoring it.

**MF02: one character crashed with a 500 and left no log entry.** `app.py::submit` rejects missing, empty, non-string, and oversized text, but nothing too short to score. One character passes validation, `detector.model_signal` raises a `ValueError` because there isn't enough text to measure, and nothing in the route catches it. Flask returns a 500, and because the error happens before `audit.log_decision` runs, the request leaves no record. A writer gets a server error and nobody can tell afterwards that it happened.

---

## The Improvement

**What I changed:** Signal two now returns a neutral 0.5 when it can't read most of the text. A new function, `stylometry.py::readable_share`, splits the text on spaces and counts how many chunks contain at least one Latin letter or digit, the only characters `words()` can see. If that share is under `MIN_READABLE_SHARE` (0.5), `style_signal` returns 0.5 before computing any features. I used a share instead of a minimum word count so a short English message is still scored normally.

**Which diagnosis pointed at it:** MF06 and MF07, the two failures with one cause. Signal two found zero readable words in emoji and Arabic, and its features fell back to a style score of 0.833, so it reported "can't measure" as "looks like AI." MF07 is also the outcome I named as the worst in the Before run. With signal two neutral, the model signal (0.997 and 0.906) and signal two (0.5) now disagree by more than 0.3, so the disagreement rule I already had turns them into "unsure."

### Attack Run — After

`python run_attacks.py --set attack_set --label after`, written to `results/attack_run_2026-11-17_0045_after.md`. Scores are from the audit log for the same run (`python attack_scores.py`, saved to `results/attack_scores_after.txt`). Same marking rules as Before.

| ID                 | Family            | Going for                                   | Status       | Guess      | Combined  | Mark                                       |
| ------------------ | ----------------- | ------------------------------------------- | ------------ | ---------- | --------- | ------------------------------------------ |
| EV01               | evasion           | typos raise word variety                    | 200          | unsure     | 0.500     | held (disagreement rule)                   |
| EV02               | evasion           | broken-up sentences                         | 200          | unsure     | 0.500     | held (disagreement rule)                   |
| EV03               | evasion           | pasted quotation                            | 200          | unsure     | 0.500     | held (disagreement rule)                   |
| EV04               | evasion           | unusual words raise perplexity              | 200          | unsure     | 0.638     | held                                       |
| EV05               | evasion           | heavy human editing pass                    | 200          | unsure     | 0.283     | held                                       |
| EV06               | evasion           | one very long, one very short sentence      | 200          | unsure     | 0.445     | held                                       |
| EV07               | evasion           | padding with punctuation                    | 200          | unsure     | 0.413     | held                                       |
| EV08               | evasion           | text below the token window                 | 200          | unsure     | 0.500     | held (disagreement rule)                   |
| EV09               | evasion           | human opening bolted on                     | 200          | unsure     | 0.513     | held                                       |
| EV10               | evasion           | repeated stanza structure                   | 200          | ai         | 0.867     | held (caught)                              |
| FP01               | false positive    | plain human writing                         | 200          | unsure     | 0.565     | held                                       |
| FP02               | false positive    | formal register                             | 200          | unsure     | 0.743     | held                                       |
| FP03               | false positive    | non-native English speaker                  | 200          | unsure     | 0.678     | held                                       |
| FP04               | false positive    | student essay to a rubric                   | 200          | unsure     | 0.666     | held                                       |
| **FP05**           | false positive    | technical documentation by a person         | 200          | **ai**     | **0.854** | **broke** (unchanged)                      |
| FP06               | false positive    | formal letter template                      | 200          | unsure     | 0.500     | held (disagreement rule)                   |
| FP07               | false positive    | deliberate repetition                       | 200          | unsure     | 0.731     | held                                       |
| FP08               | false positive    | very short human submission                 | 200          | unsure     | 0.417     | held                                       |
| PI01               | prompt injection  | instruction to ignore the check             | 200          | unsure     | 0.372     | held                                       |
| PI02               | prompt injection  | fake system message                         | 200          | unsure     | 0.217     | held (0.017 above the human line)          |
| PI03               | prompt injection  | instruction in the writer's voice           | 200          | unsure     | 0.389     | held                                       |
| PI04               | prompt injection  | hostile label text                          | 200          | unsure     | 0.442     | held                                       |
| PI05               | prompt injection  | inject fields into the audit log            | 200          | unsure     | 0.500     | held                                       |
| PI06               | prompt injection  | instruction plus real human text            | 200          | unsure     | 0.549     | held                                       |
| MF01               | malformed         | whitespace only                             | 400          |            |           | held                                       |
| **MF02**           | malformed         | single character                            | **500**      |            |           | **broke** (unchanged, crash, no log entry) |
| MF03               | malformed         | control characters                          | 200          | unsure     | 0.500     | held                                       |
| MF04               | malformed         | punctuation only                            | 200          | unsure     | 0.500     | held                                       |
| MF05               | malformed         | one very long word                          | 200          | unsure     | 0.500     | held                                       |
| MF06               | malformed         | emoji only                                  | 200          | **unsure** | **0.500** | **held (was broke at 0.882)**              |
| MF07               | malformed         | right-to-left script (Arabic)               | 200          | **unsure** | **0.500** | **held (was broke at 0.855)**              |
| MF08               | malformed         | 60,000 characters                           | 400          |            |           | held                                       |
| RQ01 to RQ12       | malformed request | missing fields, wrong types, bad JSON, etc. | 400 (all 12) |            |           | held                                       |
| FL01_01 to FL01_08 | flood             | rate limit fails                            | 200          | unsure     | 0.500     | held                                       |
| FL01_09 to FL01_12 | flood             | rate limit fails                            | 429          |            |           | held                                       |

**Count: 54 held, 2 broke** (FP05, MF02). Before: 52 held, 4 broke.

**Did it help, and how do I know:** Yes, for the two attacks it targeted, and it went through the mechanism I expected. MF06 and MF07 both now show a style score of exactly 0.500 in the audit log, a gap to the model score of 0.497 and 0.406, and a combined score of 0.500 from the disagreement rule. Every other attack has the same combined score as the Before run, so the change didn't move anything it wasn't meant to. My five criteria also came out identical (`python run_eval.py --label after`, `results/run_2026-11-17_0047_after.md`; `python appeal_eval.py --label after`, `results/appeals_2026-11-17_0048_after.md`), because all my test pieces are English and the new check never fires on them. Criterion 3 still misses and FP05 and MF02 still break, since this change doesn't touch them.

**What it costs:** Text in a non-Latin script can now never get a confident label in either direction. With signal two fixed at 0.5, the combined score can only land between about 0.41 and 0.59, or get sent to 0.5 by the disagreement rule. An Arabic writer can't be falsely accused anymore, but they can't get a "human" label either, and AI-generated Arabic will never be caught. It also opens a new evasion route: putting an emoji between every word of AI text drops the readable share under 0.5 and makes signal two go neutral. Right now that gains an attacker nothing, since unedited AI text already lands at "unsure" (criterion 3). But if signal two got better at catching AI, this would be a way around it. I think it's the right trade, because a wrong "AI" label on someone's own language is worse than an "unsure" on everything in that language.

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
