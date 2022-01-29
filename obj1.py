while True:
    inp = str(input("enter the Question "))
    levels = {'What': 'L1', 'Difference': 'L2', 'Explain': 'L3', 'Solve': 'L4', 'Compute': 'L4'}

    if inp in levels:
        print('Difficulty Level is ', levels[inp])
    else:
        print('Please enter a valid question...')

    if inp == '':
        break




