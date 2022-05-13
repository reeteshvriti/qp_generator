import random
import csv
from obj1 import *

with open('questions.csv', '+w') as file:
    myfile = csv.writer(file)
    # myfile.writerow(['question', 'marks'])
    print("Enter minimum 10 questions ")
    no_of_question =int(input("Please enter the no of questions: "))
    for i in range(no_of_question):
        question = input("Enter the question: ")
        if question == "":
            break
        else:
            pass
        marks = input("Enter the Marks: ")
        QA=question.split(" ")
        TagArray=[]
        for i in QA:
            Tag = level_check(i)
            if Tag != 'Please enter a valid question':
                TagArray.append(Tag)

        TagArray.sort()
        print(TagArray)
        myfile.writerow([question, marks,"L"+str(TagArray[len(TagArray)-1])])

file = 'questions.csv'
nquestions = open('questions.csv')
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


for i in range(0, len(newRow)//2):
    randomGen()

mode = "r"
with open(file=file, mode=mode) as myfile:

    csv_reader = csv.reader(myfile)

    questions_entered = list(csv_reader)
    print("-------------------------------------------")

    print("The questions  entered are")

    for line in questions_entered:

        for word in line:

            print(word,'\t',end=' ')

        print()
print("-------------------------------------------")

print("The questions generated are: ")
print('Question', "marks", "level")
for i in newRandom:
    print(*newRow[i])
