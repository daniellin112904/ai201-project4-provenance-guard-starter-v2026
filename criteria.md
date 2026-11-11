# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. _"The
detector is accurate"_ is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. _"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"_ is a criterion.

Under each, write a sentence or two on **why that target**. _"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"_ is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area            | A question it could answer                                    |
| --------------- | ------------------------------------------------------------- |
| False positives | How often may a human's writing get called AI?                |
| Score spread    | How far apart should clearly-AI and clearly-human text score? |
| Label coverage  | Is every one of your three labels actually reachable?         |
| The appeal path | Does an appeal always change status and always get recorded?  |
| Bad input       | What happens when `text` is missing, empty, or enormous?      |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---

## 1. False positives on my own writing

Of 10 pieces I wrote myself, including at least 4 formal ones (class essays or professional emails), at most 1 is labeled high-confidence AI.

**Why this target:**
A wrong accusation costs a real writer far more than a missed piece of AI text costs the site, especially a student whose grade or reputation could depend on it. Allowing 1 in 10 still admits the detector isn't perfect, but 2 or more would mean it's flagging genuine writing often enough that no writer could trust it. I include formal writing deliberately: it's what my false positive trace says is most likely to get flagged, and leaving it out would make the number look better without testing the weakness.

---

## 2. Score spread between clearly-AI and clearly-human text

The average combined score of 5 unedited chatbot responses is at least 0.40 higher than the average combined score of 5 casual pieces I wrote myself (messages, notes, informal posts).

**Why this target:**
A system that labels everything "unsure" would pass my false positive criterion without detecting anything. This gap proves the score actually separates the two. I'd expect AI text around 0.85 to 0.9 and casual human text around 0.3 to 0.4, so 0.40 is the smallest gap that still puts the two groups on opposite sides of my unsure band rather than both inside it.

---

## 3. Unedited AI text reaches the AI label

Of 5 unedited chatbot responses, at least 4 score 0.85 or higher and receive the high-confidence AI label.

**Why this target:**
My AI threshold is deliberately high to protect human writers, which risks a label that's never actually used. If clearly AI-generated text can't reach 0.85, the high-confidence AI label exists only on paper. Allowing 1 miss in 5 admits that some AI text will land in "unsure", which my design accepts on purpose.

---

## 4. Every appeal is recorded and changes status

10 of 10 valid appeals, each on a different real `content_id`, return `under_review`, record the writer's reasoning, and add a new entry to the audit log while the original decision entry stays unchanged. An appeal on a `content_id` that doesn't exist returns 404.

**Why this target:**
The appeal is the only protection a falsely accused writer has. If even one appeal fails silently or isn't recorded, that writer has no way to challenge the decision and no evidence they tried. Unlike detection, appeals don't depend on judgment calls, so anything less than every time is a bug.

---

## 5. Bad input is refused cleanly

10 of 10 invalid submissions, covering missing `text`, empty or whitespace-only text, a non-string `text`, missing `creator_id`, and text over 10,000 characters, return HTTP 400 with an error message that says what was wrong. None of them produce a decision: no guess, no score, and no label.

**Why this target:**
Invalid input has to be handled the same way every time. The service shouldn't crash, and it especially shouldn't hand back a score for text it never properly analyzed, since a made-up score is worse than none. 10,000 characters is about 1,500 to 2,000 words, comfortably above a long essay, so the limit only stops abuse, not real writers. A rejection may be recorded in the log as a rejected request, but it never becomes a decision.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
