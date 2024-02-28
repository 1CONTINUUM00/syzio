import random, csv
x= 0
i = 0
questions= ['howa are u feeling tday', 'how is work life','how are important relationships']
answers = []

while i<3:
    print(questions[i])
    k = int(input('on a scale of 1 to 5'))
    i+=1
    answers.append(k)

for i in answers:
    x = x+i

sum = x/ len(answers)

with open('syzio.csv', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    print(answers)
'''
    # writing the data rows
    csvwriter.writerows(list(answers))

'''