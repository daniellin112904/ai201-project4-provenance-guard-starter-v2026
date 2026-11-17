"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # 10 pieces I wrote myself. The first 5 are formal (an email to the CS
        # department and written answers from my AI201 projects); the last 5
        # are casual messages.
        "texts": [
            "Dear Ko, My name is Daniel Lin. I am a computer science transfer student and have credit up to CSCI 235. I would like to take CSCI 39542 next semester, but it has a prerequisite of CSCI 127, which I didn't get transfer credit for and will be waived when applying for graduation. I am writing to ask for permission to enroll in CSCI 39542 next semester. Please let me know if you have any questions or need anything from me. Thanks, Daniel Lin",
            "I would choose MF07 (Arabic text) as the single worst outcome. I think this is worse because the system falsely labels someone's writing as AI-generated simply because it cannot properly process their language. The stylometry signal only recognizes English letters and numbers, so Arabic text receives a high AI score regardless of how it was written. FP05 is also a serious false positive, but at least the system can analyze the text. With MF07, the system is making a confident accusation based partly on features it cannot even measure correctly. This is especially concerning because it could affect an entire group of writers rather than just certain writing styles. I would rather have the system return 'unsure' for unsupported languages than confidently label them as AI-generated.",
            "I think a sharp disagreement should always result in an 'unsure' label, regardless of whether the combined score leans toward human or AI. If the two signals differ by more than 0.3, I would move the combined score to 0.5, placing it in the unsure range. This prevents the system from making a confident decision when its two methods strongly disagree. The punctuation example shows why this matters. Changing punctuation alone shouldn't cause AI-generated text to receive a high-confidence human label, especially when the model signal still suggests otherwise. I don't think making the rule symmetric conflicts with my priority of avoiding false accusations. It actually makes the system more consistent because uncertainty should be treated the same way in both directions. I would rather have the system admit it isn't sure than confidently give an incorrect label, whether that's AI or human.",
            "I would set the human threshold at 0.20 for now. Since the lightly edited AI text scored 0.231, lowering the threshold to 0.25 wouldn't actually fix that false classification. I chose 0.20 because I don't want the system to confidently label AI-generated writing as human just because it has been slightly edited. While my main priority is avoiding false accusations against human writers, I also don't want the system to give misleading confidence in the opposite direction. The downside is that genuine human writing, like my casual message, would still receive an 'unsure' label. I'm okay with that because uncertainty is better than an incorrect confident label. However, I would need to test more samples to make sure the human label is actually reachable. If almost nothing scores below 0.20, I would reconsider the threshold based on additional results.",
            "I chose to increase the number of training epochs from 3 to 10 because the original model barely learned during training. Training loss only decreased from 1.07 to 0.94, and validation accuracy stayed at 0.472 across all three seeds. Increasing the epochs gives the model more optimization steps while keeping the learning rate and all other settings unchanged. This tests whether insufficient training time caused the model's failure to learn the three labels.",
            "ok update on fall schedule: havent heard back from any internships so far, so i think i wont have one for the fall, which is actually better for my schedule and will free up a lot of things for my classes, im doing: OS, theory, big data anal, database. then i will do one of comp sec or net sec (i didnt get off waitlist for swe. and for wi, i will see how much time the course consumes and drop if its too much. for codepath: i am doing tip, and cyb/ai201 (both at same time so i will pick one to do) and for TA: confirmed for discrete and 335 (dsa), waiting on 260 (comp arch), with around 3-5hrs per week each. what do you think about the schedule so far, and let me know if you have any questioins or need clarification on time slots before i ask you questions regarding it",
            "so from what i understand taking his class last fall: homework is not mandatory and is for practice, so barely anyone does it, so grading wont be an issue. tutoring can be online (2hrs in the morning or during the weekend), proctoring is only 1 lecture time (1hr25) and 2hrs for final. the only thing that may take longer is scanning and grading. i think it is super manageable if i dont get any internships which would free up 17-20hrs",
            "ok actually now thinking about it, if i drop computer security, i would only have one class on mw (~1hr commute to campus). so maybe network security/database/writing is the better class to drop? my schedule is: mw: os 4-5:15, comp security 5:30-6:45 tth: writing 2:30-3:45, network security 4-5:15, theory 5:30-6:45, database (online) 7-8:15 all my classes are at the evening to have time in the morning for internship and TA office hours i also have 3 choices for codepath (im choosing 1, leaning towrds tip cause i need to prepare for interviews): tip102 tth 8-10 (starts 15mins before database ends but i can juggle/attend both class for those 15mins, ai201 and cyb 101 both on wed 8-10. do you think tip is the right choice? i think i would want to do at least 5hrs for TA, 3 is just what i think the minimum might be so use 5 for calculations. also last semester, half the time no one showed up to tutoring so i had half the time free, also a lot of free time at work (to grade/study/do hw), but people say the courses im doing this semester is harder so people will show up (use up the 5hrs)",
            "yeah but she asked me what questions i want in the form.  235 is oop and 335 is dsa, i was thinking ones that are taking or finished 335. also i dont really care about the schedule or what the student wants, i just want ppl to study interviews with, and worst case i can do it with my friends. we will be professional when doing the mock",
            "i think rescheduled exams will likely happen the following semester (i wont be able to register for all classes). do you think that is something worth mentioning. also should i call the school's registrar before emailing prof regarding my situation and see if they can excuse it?",
        ],
    },
    {
        "name": "casual human",
        "criterion": 2,
        # The same 5 casual messages from above, for the score spread.
        "texts": [
            "ok update on fall schedule: havent heard back from any internships so far, so i think i wont have one for the fall, which is actually better for my schedule and will free up a lot of things for my classes, im doing: OS, theory, big data anal, database. then i will do one of comp sec or net sec (i didnt get off waitlist for swe. and for wi, i will see how much time the course consumes and drop if its too much. for codepath: i am doing tip, and cyb/ai201 (both at same time so i will pick one to do) and for TA: confirmed for discrete and 335 (dsa), waiting on 260 (comp arch), with around 3-5hrs per week each. what do you think about the schedule so far, and let me know if you have any questioins or need clarification on time slots before i ask you questions regarding it",
            "so from what i understand taking his class last fall: homework is not mandatory and is for practice, so barely anyone does it, so grading wont be an issue. tutoring can be online (2hrs in the morning or during the weekend), proctoring is only 1 lecture time (1hr25) and 2hrs for final. the only thing that may take longer is scanning and grading. i think it is super manageable if i dont get any internships which would free up 17-20hrs",
            "ok actually now thinking about it, if i drop computer security, i would only have one class on mw (~1hr commute to campus). so maybe network security/database/writing is the better class to drop? my schedule is: mw: os 4-5:15, comp security 5:30-6:45 tth: writing 2:30-3:45, network security 4-5:15, theory 5:30-6:45, database (online) 7-8:15 all my classes are at the evening to have time in the morning for internship and TA office hours i also have 3 choices for codepath (im choosing 1, leaning towrds tip cause i need to prepare for interviews): tip102 tth 8-10 (starts 15mins before database ends but i can juggle/attend both class for those 15mins, ai201 and cyb 101 both on wed 8-10. do you think tip is the right choice? i think i would want to do at least 5hrs for TA, 3 is just what i think the minimum might be so use 5 for calculations. also last semester, half the time no one showed up to tutoring so i had half the time free, also a lot of free time at work (to grade/study/do hw), but people say the courses im doing this semester is harder so people will show up (use up the 5hrs)",
            "yeah but she asked me what questions i want in the form.  235 is oop and 335 is dsa, i was thinking ones that are taking or finished 335. also i dont really care about the schedule or what the student wants, i just want ppl to study interviews with, and worst case i can do it with my friends. we will be professional when doing the mock",
            "i think rescheduled exams will likely happen the following semester (i wont be able to register for all classes). do you think that is something worth mentioning. also should i call the school's registrar before emailing prof regarding my situation and see if they can excuse it?",
        ],
    },
    {
        "name": "chatbot responses",
        "criterion": 3,
        # 5 unedited chatbot responses (written by Claude for this test). Used
        # for criterion 3 and for the AI side of criterion 2.
        "texts": [
            "Compound interest is interest calculated on both the initial principal and the interest that has already been added to it. In other words, you earn interest on your interest. For example, if you invest $1,000 at an annual rate of 5%, you would have $1,050 after the first year. In the second year, the 5% is applied to $1,050 rather than the original $1,000, giving you $1,102.50. Over time, this effect grows significantly, which is why starting to save early can make such a large difference. The frequency of compounding also matters. Interest that compounds monthly or daily will grow slightly faster than interest that compounds annually. The same principle works against you with debt, since unpaid credit card balances can grow quickly when interest compounds. Understanding compound interest can help you make better decisions about saving, investing, and borrowing.",
            "Managing your time well in college is one of the most important skills you can develop. Start by using a planner or digital calendar to keep track of classes, assignment due dates, and exams. At the beginning of each week, review your schedule and set specific goals for what you want to accomplish. Breaking large projects into smaller tasks can make them feel more manageable and help you avoid last-minute stress. It is also helpful to identify the times of day when you are most focused and reserve those hours for your most demanding work. Try to limit distractions by silencing notifications or studying in a quiet space like the library. Finally, remember to schedule time for rest, exercise, and social activities. Maintaining a healthy balance will help you stay motivated and perform better academically throughout the semester.",
            "Photosynthesis is the process plants use to convert light energy into chemical energy. It takes place mainly in the chloroplasts, which contain a green pigment called chlorophyll. Chlorophyll absorbs sunlight, which provides the energy needed to drive the process. During photosynthesis, plants take in carbon dioxide from the air through small openings in their leaves called stomata, and they absorb water through their roots. Using the energy from sunlight, they convert these ingredients into glucose and oxygen. The glucose serves as a source of energy and building material for the plant, while the oxygen is released into the atmosphere. Photosynthesis occurs in two main stages: the light-dependent reactions and the Calvin cycle. This process is essential for life on Earth because it produces the oxygen we breathe and forms the foundation of most food chains.",
            "Sleep plays a vital role in both physical and mental health. During sleep, your body repairs tissues, strengthens the immune system, and regulates important hormones. Your brain also uses this time to process information and consolidate memories, which is why a good night's sleep can improve learning and concentration. Most adults need between seven and nine hours of sleep each night to function at their best. Not getting enough sleep can lead to difficulty focusing, irritability, and a weakened immune system. Over time, chronic sleep deprivation has been linked to more serious health problems, including heart disease, diabetes, and depression. To improve your sleep, try to maintain a consistent schedule, limit screen time before bed, and create a cool, dark, and quiet sleeping environment. Prioritizing sleep is one of the simplest ways to support your overall well-being.",
            "Learning to code is a rewarding journey, and the best way to start is by choosing a beginner-friendly programming language. Python is often recommended because its syntax is clear and easy to read. Once you have chosen a language, take advantage of free online resources such as interactive tutorials, video courses, and coding practice websites. It is important to practice consistently, even if it is only for a short time each day. As you learn the basics, try building small projects like a calculator, a to-do list, or a simple game. Projects help you apply what you have learned and develop problem-solving skills. Do not be discouraged by errors, since debugging is a normal and valuable part of programming. Finally, consider joining online communities where you can ask questions, share your progress, and learn from others.",
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        # The cases criterion 5 names: missing text, empty or whitespace-only
        # text, non-string text, missing creator_id, and text over 10,000
        # characters. Every one should return 400 with no decision.
        "bodies": [
            {"creator_id": "eval_bad_no_text"},                          # missing text
            {"text": None, "creator_id": "eval_bad_null"},               # text is null
            {"text": "", "creator_id": "eval_bad_empty"},                # empty
            {"text": "   \n\t  ", "creator_id": "eval_bad_whitespace"},  # whitespace only
            {"text": 42, "creator_id": "eval_bad_number"},               # non-string: number
            {"text": ["a", "b"], "creator_id": "eval_bad_list"},         # non-string: list
            {"text": {"a": 1}, "creator_id": "eval_bad_object"},         # non-string: object
            {"text": "This is real writing with no creator attached."},  # missing creator_id
            {"text": "This is real writing.", "creator_id": ""},         # empty creator_id
            {"text": "word " * 2001, "creator_id": "eval_bad_huge"},     # 10,005 characters
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
