import random
import csv
from obj1 import *
# from pdf_gen import *
# from sum import *


with open('questions_entered.csv', 'w',  newline='') as file:
    myfile = csv.writer(file)
    no_of_question =int(input("Please enter the no of questions: "))
    # SL_NO=0
    for i in range(no_of_question):
        question = input("Enter the question: ")
        if question == "":
            break
        else:
            pass
        marks = int(input("Enter the Marks: "))
        co = input("enter the Course Outcome: ")
        QA=question.split(" ")
        TagArray=[]

        for i in QA:
            Tag = level_check(i)
            if Tag != 'Please enter a valid question':
                TagArray.append(Tag)
                print(TagArray)
        TagArray.sort()
        # SL_NO=SL_NO+1
        myfile.writerow([question, marks, co, "L"+str(TagArray[len(TagArray)-1])])


file = 'questions_entered.csv'
nquestions = open('questions_entered.csv')
csvreader = csv.reader(nquestions)
newRow=[]
for row in csvreader:
    if row !=[]:
        newRow.append(row)

newRandom = []
def randomGen():
     newNumber=random.choice(range(0, len(newRow)))
     if newNumber in newRandom:
         randomGen()
     else:
         newRandom.append(newNumber)


for i in range(0, len(newRow)//1):
    randomGen()

mode = "r"
with open(file=file, mode=mode) as myfile:

    csv_reader = csv.reader(myfile)

    questions_entered = list(csv_reader)
    print("-------------------------------------------")

    print("The questions  entered are")

    for line in questions_entered:

        for word in line:

            print(word, '\t', end=' ')

        print()
print("-------------------------------------------")


file_output = open('random_generated.csv', '+w', newline='')
csv_writer = csv.writer(file_output, delimiter=',')


for i in newRandom:
    csv_writer.writerow(newRow[i])