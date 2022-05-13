def level_check(key):
    if key in ['Choose', 'Define', 'Find', 'How', 'Label', 'List', 'Match', 'Name', 'Omit', 'Recall', 'Spell',
               'Tell', 'What', 'When', 'Where', 'Which', 'Who', 'Why']:
        return 1

    elif key in ['Explain', 'Extend', 'Illustrate', 'Infer',
                 'Outline', 'Relate', 'Rephrase', 'Show', 'Summarize', 'Translate']:
        return 2

    elif key in ['Apply', 'Build', 'Develop', 'Experiment	with', 'Identify', 'Make', 'use of',
                 'Model', 'Organize', 'Plan', 'Select', 'Solve', 'Utilize']:

        return 3
    elif key in ['Analyze', 'Assume', 'Categorize', 'Classify', 'Compare', 'Conclusion', 'Contrast', 'Discover',
                 'Dissect', 'Distinguish',
                 'Divide', 'Examine', 'Function', 'Inference', 'Inspect', 'Motive', 'Relationships', 'Simplify',
                 'Survey', 'Take	part	in', 'Test	for', 'Theme']:

        return 4
    elif key in ['Agree', 'Appraise', 'Assess', 'Award', 'Conclude', 'Criteria', 'Criticize', 'Decide', 'Deduct',
                 'Defend',
                 'Determine', 'Disprove', 'Estimate', 'Evaluate', 'Importance', 'Influence', 'Interpret', 'Judge',
                 ' Justify', 'Mark', 'Measure',
                 'Opinion', 'Perceive', 'Prioritize', 'Prove', 'Rate', 'Recommend', 'Rule on', 'Support', 'Value']:

        return 5
    elif key in ['Adapt', 'Build', 'Change', 'Combine', 'Compile', 'Compose', 'Construct', 'Create', 'Delete',
                 'Design', 'Develop', 'Discuss', 'Elaborate', 'Formulate', 'Happen', 'Imagine', 'Improve', 'Invent',
                 'Make up',
                 'Maximize', 'Minimize', 'Modify', 'Original', 'Originate', 'Plan', 'Predict', 'Propose', 'Solution',
                 'Suppose',
                 'Test', 'Theory']:

        return 6
    else:
        return "Please enter a valid question"
