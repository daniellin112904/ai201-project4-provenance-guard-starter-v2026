# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-17 00:45
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `84980087-60f3-400b-8e8f-9aed3759bb71` | unsure | 0.500 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `09c45cb2-d01b-49e6-ac61-7d41c03d7741` | unsure | 0.500 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `cd339cf9-8aed-4df5-94d9-b021359004d0` | unsure | 0.500 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `8ad98bfb-5aad-4412-aea6-1f313626c912` | unsure | 0.638 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `daca7a9c-3f8e-498c-a689-421d681ef9cd` | unsure | 0.283 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `bdbd9641-6ea7-45d0-8b83-30e6c6f8323e` | unsure | 0.445 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `859dbf81-5e44-4233-9b9d-f2f868955890` | unsure | 0.413 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `5563b2f1-f5e8-46df-94f7-f25d2bfd508b` | unsure | 0.500 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `a56937fe-07df-4821-8952-8bcbe9694550` | unsure | 0.513 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `131ff9bf-7f33-4a3b-81a5-4d4f23431e51` | ai | 0.867 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `792d97be-124e-42ea-93fa-7839a6167d04` | unsure | 0.565 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `c8939904-c7dc-4777-99c8-b9d79967c867` | unsure | 0.743 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `24f01df5-a2b3-469c-9e08-8e81807361dc` | unsure | 0.678 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `89eece4d-23d7-4d8b-9b3c-e16db561c318` | unsure | 0.666 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `f024c832-3305-4f2f-87eb-21be1d76e2be` | ai | 0.854 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `c0ee7a6c-af49-4766-aa3f-49a10b88a3f6` | unsure | 0.500 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `1ffe21bf-47c1-4515-9dd8-00679bd2327d` | unsure | 0.731 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `854d5c99-1223-4f2a-a3fe-02b0470dd25b` | unsure | 0.417 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `66129fde-decb-4528-9db9-49f62f77ad2f` | unsure | 0.372 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `80597b4e-2ce4-426b-900c-e3bf66d632a5` | unsure | 0.217 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `9ad77192-f189-4aee-a1e0-ffd7b36f7dd4` | unsure | 0.389 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `3f319443-cdf3-430d-b975-3c6c4b391a94` | unsure | 0.442 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `5de548fc-c30b-463a-b73a-484a557e961b` | unsure | 0.500 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c27b9931-cd2c-4d67-99a8-871f4ca169e2` | unsure | 0.549 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `435d42d3-7847-4695-987b-9f07ea53979f` | unsure | 0.500 |  |
| MF04 | malformed | text is only punctuation | 200 | `eab54e86-e160-41ba-ac1a-d5eb3967981e` | unsure | 0.500 |  |
| MF05 | malformed | text is a very long single word | 200 | `27e6bd8d-9db7-40af-8f20-7343121c711a` | unsure | 0.500 |  |
| MF06 | malformed | text is emoji only | 200 | `233616e2-7ff2-4d3b-8f71-8ed3e0c6448f` | unsure | 0.500 |  |
| MF07 | malformed | text is right-to-left script | 200 | `9a8dc58b-7d25-4230-ba42-073a034155bf` | unsure | 0.500 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `996095bb-53c3-450e-b1cf-71bde96cb42e` | unsure | 0.500 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0eff070f-b461-44e6-9507-cba06ac1c144` | unsure | 0.500 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dbe53c16-6ac1-48c5-916f-4ec442a9c04c` | unsure | 0.500 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b8b14ac0-a33b-494e-b2ed-81f1a269c73f` | unsure | 0.500 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `00fa83b5-8c88-49a5-989f-786d798c4781` | unsure | 0.500 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8a3dc831-bdd3-402b-a3a3-6641d2c45800` | unsure | 0.500 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a959d003-a0d9-4c21-a64f-6208e80fb9da` | unsure | 0.500 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `54499b76-6cba-429a-9fba-83af274f37f7` | unsure | 0.500 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "84980087-60f3-400b-8e8f-9aed3759bb71",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.1635,
  "style_score": 0.6587,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "09c45cb2-d01b-49e6-ac61-7d41c03d7741",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.5943,
  "style_score": 0.2286,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "cd339cf9-8aed-4df5-94d9-b021359004d0",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.6662,
  "style_score": 0.116,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "8ad98bfb-5aad-4412-aea6-1f313626c912",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6376,
  "model_score": 0.6114,
  "style_score": 0.6489,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "daca7a9c-3f8e-498c-a689-421d681ef9cd",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.2835,
  "model_score": 0.3212,
  "style_score": 0.2674,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "bdbd9641-6ea7-45d0-8b83-30e6c6f8323e",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4449,
  "model_score": 0.5727,
  "style_score": 0.3902,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "859dbf81-5e44-4233-9b9d-f2f868955890",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4127,
  "model_score": 0.5862,
  "style_score": 0.3384,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "5563b2f1-f5e8-46df-94f7-f25d2bfd508b",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.2452,
  "style_score": 0.5683,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "a56937fe-07df-4821-8952-8bcbe9694550",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5133,
  "model_score": 0.7042,
  "style_score": 0.4315,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "131ff9bf-7f33-4a3b-81a5-4d4f23431e51",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8673,
  "model_score": 0.9792,
  "style_score": 0.8193,
  "label": "This writing shows strong signs of being AI-generated. However, this is only an estimate and does not necessarily mean AI was used. If you believe this result is incorrect, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "792d97be-124e-42ea-93fa-7839a6167d04",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5654,
  "model_score": 0.6175,
  "style_score": 0.543,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "c8939904-c7dc-4777-99c8-b9d79967c867",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7428,
  "model_score": 0.7387,
  "style_score": 0.7446,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "24f01df5-a2b3-469c-9e08-8e81807361dc",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.6785,
  "model_score": 0.8051,
  "style_score": 0.6242,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "89eece4d-23d7-4d8b-9b3c-e16db561c318",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6656,
  "model_score": 0.8329,
  "style_score": 0.5939,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "f024c832-3305-4f2f-87eb-21be1d76e2be",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.8543,
  "model_score": 0.8005,
  "style_score": 0.8774,
  "label": "This writing shows strong signs of being AI-generated. However, this is only an estimate and does not necessarily mean AI was used. If you believe this result is incorrect, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "c0ee7a6c-af49-4766-aa3f-49a10b88a3f6",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.8814,
  "style_score": 0.5532,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "1ffe21bf-47c1-4515-9dd8-00679bd2327d",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.7312,
  "model_score": 0.8816,
  "style_score": 0.6667,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "854d5c99-1223-4f2a-a3fe-02b0470dd25b",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4166,
  "model_score": 0.3223,
  "style_score": 0.457,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "66129fde-decb-4528-9db9-49f62f77ad2f",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.3721,
  "model_score": 0.4625,
  "style_score": 0.3333,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "80597b4e-2ce4-426b-900c-e3bf66d632a5",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.2169,
  "model_score": 0.2044,
  "style_score": 0.2222,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "9ad77192-f189-4aee-a1e0-ffd7b36f7dd4",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.3893,
  "model_score": 0.5943,
  "style_score": 0.3014,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "3f319443-cdf3-430d-b975-3c6c4b391a94",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.442,
  "model_score": 0.4998,
  "style_score": 0.4173,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "5de548fc-c30b-463a-b73a-484a557e961b",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.6401,
  "style_score": 0.2064,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "c27b9931-cd2c-4d67-99a8-871f4ca169e2",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5491,
  "model_score": 0.5583,
  "style_score": 0.5451,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "435d42d3-7847-4695-987b-9f07ea53979f",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "eab54e86-e160-41ba-ac1a-d5eb3967981e",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "27e6bd8d-9db7-40af-8f20-7343121c711a",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "233616e2-7ff2-4d3b-8f71-8ed3e0c6448f",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "9a8dc58b-7d25-4230-ba42-073a034155bf",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "996095bb-53c3-450e-b1cf-71bde96cb42e",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "0eff070f-b461-44e6-9507-cba06ac1c144",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "dbe53c16-6ac1-48c5-916f-4ec442a9c04c",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "b8b14ac0-a33b-494e-b2ed-81f1a269c73f",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "00fa83b5-8c88-49a5-989f-786d798c4781",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "8a3dc831-bdd3-402b-a3a3-6641d2c45800",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "a959d003-a0d9-4c21-a64f-6208e80fb9da",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "54499b76-6cba-429a-9fba-83af274f37f7",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We couldn't confidently determine whether this writing was created by a person or AI. This does not mean your writing is AI-generated, only that our system doesn't have enough evidence to make a reliable decision.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
