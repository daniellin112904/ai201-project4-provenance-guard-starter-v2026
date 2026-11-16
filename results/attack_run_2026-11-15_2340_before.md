# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-15 23:40
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `2f03fa6c-1339-46db-ada7-db6a9e479b36` | unsure | 0.500 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `4d432be5-a372-4e8b-afa9-bf3c2cecee9d` | unsure | 0.500 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `a7141f00-b97b-4f15-9af8-a6934075b940` | unsure | 0.500 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `f8d3a752-75ed-4cc0-b65f-a2d8db4410e5` | unsure | 0.638 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `088ef66b-cf60-4923-9179-916111f4fa2c` | unsure | 0.283 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `46a6b335-a576-44da-9464-d5c3b2f054d8` | unsure | 0.445 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `37329396-595f-4e1d-a0b0-acabbf605054` | unsure | 0.413 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `468670dc-b913-456d-bdc9-d7eb79e5cca5` | unsure | 0.500 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `5e66630a-a11b-44bb-baf7-7d55535e8d88` | unsure | 0.513 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `f0c919b9-2e1a-4453-8404-432671ae29dc` | ai | 0.867 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `61e41457-6405-4b45-9774-94a405bf9458` | unsure | 0.565 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `dd56b16c-8e36-41b6-8046-897219ad0ce7` | unsure | 0.743 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `007011b3-03ff-4458-8937-a1e84e2c23f6` | unsure | 0.678 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `81bc8f3f-0cc7-4ace-b7f6-4552443f9c76` | unsure | 0.666 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `269d27a3-f4dd-42f5-9503-e166ee2d8acf` | ai | 0.854 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `5c2d3612-17b2-4c42-a12b-356ba5fe225c` | unsure | 0.500 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `45485501-2435-4efe-b984-00c4004143cd` | unsure | 0.731 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `f1ba0ee8-ad0b-4cd3-a83d-57c24f62674b` | unsure | 0.417 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `6d835664-6011-4f5f-8bbd-9e7438d74494` | unsure | 0.372 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `1063767e-d8ad-4a7e-ae15-461ca97677a6` | unsure | 0.217 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `894fb9bf-bb75-44d6-89cb-6f5dcfc576e7` | unsure | 0.389 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `9d3a3233-5861-4d62-b15a-ef41eaacbcd5` | unsure | 0.442 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `4bf24004-ce15-465e-bfca-428b896ed9d1` | unsure | 0.500 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `29cf265a-843b-4596-9112-e7070cdbab0a` | unsure | 0.549 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `05bd6da2-0c3d-4a86-a664-ea7e4e33ba80` | unsure | 0.500 |  |
| MF04 | malformed | text is only punctuation | 200 | `2b75c48e-d640-4941-9cb6-3ca560356119` | unsure | 0.500 |  |
| MF05 | malformed | text is a very long single word | 200 | `fdec25ce-796d-47cd-a449-5d907a86614f` | unsure | 0.500 |  |
| MF06 | malformed | text is emoji only | 200 | `39d0d746-a179-4abb-b52f-7d77b1131c7a` | ai | 0.882 |  |
| MF07 | malformed | text is right-to-left script | 200 | `045d61c9-fbf9-4f64-8c0c-411969dfdf81` | ai | 0.855 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d3e92d16-267c-4c57-84b6-4801d3af6ff8` | unsure | 0.500 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b0312a4f-f1da-4884-8088-a51b51cb2592` | unsure | 0.500 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0e551da3-9bf3-46ce-810a-21b16cb8eafa` | unsure | 0.500 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f01eda0a-c8b4-47ec-a78a-7f0d2a666a2a` | unsure | 0.500 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `317398c5-75c9-432f-a97f-95d65843d493` | unsure | 0.500 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d0b81219-8d90-42d5-a165-569655177fae` | unsure | 0.500 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3e2f9841-53f9-467e-b7ae-f0992230a432` | unsure | 0.500 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6a651335-3062-4df8-bce2-9dbb80de1a61` | unsure | 0.500 |  |
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
  "content_id": "2f03fa6c-1339-46db-ada7-db6a9e479b36",
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
  "content_id": "4d432be5-a372-4e8b-afa9-bf3c2cecee9d",
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
  "content_id": "a7141f00-b97b-4f15-9af8-a6934075b940",
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
  "content_id": "f8d3a752-75ed-4cc0-b65f-a2d8db4410e5",
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
  "content_id": "088ef66b-cf60-4923-9179-916111f4fa2c",
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
  "content_id": "46a6b335-a576-44da-9464-d5c3b2f054d8",
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
  "content_id": "37329396-595f-4e1d-a0b0-acabbf605054",
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
  "content_id": "468670dc-b913-456d-bdc9-d7eb79e5cca5",
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
  "content_id": "5e66630a-a11b-44bb-baf7-7d55535e8d88",
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
  "content_id": "f0c919b9-2e1a-4453-8404-432671ae29dc",
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
  "content_id": "61e41457-6405-4b45-9774-94a405bf9458",
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
  "content_id": "dd56b16c-8e36-41b6-8046-897219ad0ce7",
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
  "content_id": "007011b3-03ff-4458-8937-a1e84e2c23f6",
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
  "content_id": "81bc8f3f-0cc7-4ace-b7f6-4552443f9c76",
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
  "content_id": "269d27a3-f4dd-42f5-9503-e166ee2d8acf",
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
  "content_id": "5c2d3612-17b2-4c42-a12b-356ba5fe225c",
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
  "content_id": "45485501-2435-4efe-b984-00c4004143cd",
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
  "content_id": "f1ba0ee8-ad0b-4cd3-a83d-57c24f62674b",
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
  "content_id": "6d835664-6011-4f5f-8bbd-9e7438d74494",
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
  "content_id": "1063767e-d8ad-4a7e-ae15-461ca97677a6",
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
  "content_id": "894fb9bf-bb75-44d6-89cb-6f5dcfc576e7",
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
  "content_id": "9d3a3233-5861-4d62-b15a-ef41eaacbcd5",
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
  "content_id": "4bf24004-ce15-465e-bfca-428b896ed9d1",
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
  "content_id": "29cf265a-843b-4596-9112-e7070cdbab0a",
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
  "content_id": "05bd6da2-0c3d-4a86-a664-ea7e4e33ba80",
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
  "content_id": "2b75c48e-d640-4941-9cb6-3ca560356119",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0112,
  "style_score": 0.6667,
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
  "content_id": "fdec25ce-796d-47cd-a449-5d907a86614f",
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
  "content_id": "39d0d746-a179-4abb-b52f-7d77b1131c7a",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.8824,
  "model_score": 0.9969,
  "style_score": 0.8333,
  "label": "This writing shows strong signs of being AI-generated. However, this is only an estimate and does not necessarily mean AI was used. If you believe this result is incorrect, you can submit an appeal.",
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
  "content_id": "045d61c9-fbf9-4f64-8c0c-411969dfdf81",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.8552,
  "model_score": 0.9064,
  "style_score": 0.8333,
  "label": "This writing shows strong signs of being AI-generated. However, this is only an estimate and does not necessarily mean AI was used. If you believe this result is incorrect, you can submit an appeal.",
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
  "content_id": "d3e92d16-267c-4c57-84b6-4801d3af6ff8",
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
  "content_id": "b0312a4f-f1da-4884-8088-a51b51cb2592",
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
  "content_id": "0e551da3-9bf3-46ce-810a-21b16cb8eafa",
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
  "content_id": "f01eda0a-c8b4-47ec-a78a-7f0d2a666a2a",
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
  "content_id": "317398c5-75c9-432f-a97f-95d65843d493",
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
  "content_id": "d0b81219-8d90-42d5-a165-569655177fae",
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
  "content_id": "3e2f9841-53f9-467e-b7ae-f0992230a432",
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
  "content_id": "6a651335-3062-4df8-bce2-9dbb80de1a61",
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
