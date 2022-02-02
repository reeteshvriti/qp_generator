def level_check(key):
    if key in ['Choose', 'Define', 'Find', 'How', 'Label', 'List', 'Match', 'Name', 'Omit', 'Recall', 'Relate', 'Select', 'Show', 'Spell',
               'Tell', 'What', 'When', 'Where', 'Which', 'Who', 'Why']:
        print('Level : L1')

    elif key in [' Classify', 'Compare', 'Contrast', 'Demonstrate', 'Explain', 'Extend', 'Illustrate', 'Infer', 'Interpret',
                 'Outline', 'Relate', 'Rephrase', 'Show', 'Summarize', 'Translate']:
        print('Level : L2')

    elif key in ['Apply', 'Build', 'Choose', 'Develop', 'Expirement', 'Experiment	with', 'Identify', 'Interview', 'Make',	'use of',
                'Model', 'Organize', 'Plan', 'Select', 'Solve', 'Utilize']:
        print("Level : L3")

    elif key in ['Analyze', 'Assume', 'Categorize', 'Classify', 'Compare', 'Conclusion', 'Contrast', 'Discover', 'Dissect', 'Distinguish',
                 'Divide', 'Examine', 'Function',   'Inference', 'Inspect', 'List', 'Motive', 'Relationships', 'Simplify',
                 'Survey', 'Take	part	in', 'Test	for', 'Theme']:
        print("Level : L4")

    elif key in ['Explain', 'Agree', 'Appraise', 'Assess', 'Award', 'Choose', 'Compare', 'Conclude', 'Criteria', 'Criticize', 'Decide', 'Deduct', 'Defend',
                 'Determine', 'Disprove', 'Estimate', 'Evaluate', 'Importance', 'Influence', 'Interpret', 'Judge', ' Justify', 'Mark', 'Measure',
                 'Opinion', 'Perceive', 'Prioritize', 'Prove', 'Rate', 'Recommend', 'Rule on', 'Select', 'Support', 'Value' ]:
        print("Level : L5")

    elif key in ['Adapt','Build', 'Change','Choose', 'Combine','Compile', 'Compose', 'Construct', 'Create', 'Delete',
                 'Design', 'Develop','Discuss','Elaborate','Estimate', 'Formulate', 'Happen', 'Imagine', 'Improve', 'Invent', 'Make up',
                 'Maximize','Minimize', 'Modify', 'Original', 'Originate', 'Plan', 'Predict', 'Propose', 'Solution', 'Solve', 'Suppose',
                 'Test', 'Theory']:
        print("Level : L6")

    else:
        print("Please enter a valid question")



while True:
    ip=input("Enter the question ")
    eq = ip.split()
    print(f"Question Entered :  {ip}")
    if ip=="":
        break
    else:
        level_check(eq[0])