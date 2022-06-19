import csv
csv_file = open('random_generated.csv', encoding="utf8")
csv_data = csv.reader(csv_file, delimiter=',')


file_output = open('questions_generated.csv', '+w', newline='')
csv_writer = csv.writer(file_output, delimiter=',')

data_lines = list(csv_data)
levels_list = []
levels_SL_No = []
levels_question = []
levels={'L1':1, "L2":3,  "L6":1}
Sl_No = 0
for i in levels:
    for question in data_lines:
        res=levels_list.count(i)
        if question[3]==i and res<levels[i] and levels_SL_No.count(question[0])!=1:
            levels_list.append(question[3])
            levels_SL_No.append(question[0])
            levels_question.append((question[1]))
            Sl_No=Sl_No+1
            csv_writer.writerow([Sl_No,question[0], question[1],question[2], question[3]])


# print(levels_list)
# print(levels_question)

