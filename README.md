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

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**

**The numbers:**

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label                 | Score range | The exact text a reader sees |
| --------------------- | ----------- | ---------------------------- |
| high-confidence human |             |                              |
| unsure                |             |                              |
| high-confidence AI    |             |                              |

**Why I worded the "unsure" one this way:**

<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'
```

```json

```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json

```

---

## How I Used AI

**Moment 1**

- _What I asked for:_
- _What came back:_
- _What I changed:_

**Moment 2**

- _What I asked for:_
- _What came back:_
- _What I changed:_

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** **_ per minute, _** per day

**Why those numbers and not others:**

<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
| --------- | ------ | ----- | ----- | ----- | ------- |
| 1.        |        |       |       |       |         |
| 2.        |        |       |       |       |         |
| 3.        |        |       |       |       |         |
| 4.        |        |       |       |       |         |
| 5.        |        |       |       |       |         |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

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

---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

**Did it help, and how do I know:**

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
