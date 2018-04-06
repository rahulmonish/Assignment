import numpy as np
Marks_dataset = {}
marks_list = []
for i in range(0,3):
    name = input("Enter the name of student")
    print("Enter 3 subject marks")
    for j in range(0,3):
        marks_list.append(int(input()))
        Marks_dataset[name] = marks_list
    marks_list = []

subject_1 = []
subject_2 = []
subject_3 = []

for i in Marks_dataset.values():
    subject_1.append(i[0])
    subject_2.append(i[1])
    subject_3.append(i[2])

print("Mean of 1st subject", np.mean(subject_1))
print("Mean of 2st subject", np.mean(subject_2))
print("Mean of 3st subject", np.mean(subject_3))

print("Median of 1st subject", np.median(subject_1))
print("Median of 2st subject", np.median(subject_2))
print("Median of 3st subject", np.median(subject_3))

subject_marks_sheet = {}
subject_1.sort()
subject_2.sort()
subject_3.sort()

subject_marks_sheet['subject_1'] = subject_1
subject_marks_sheet['subject_2'] = subject_2
subject_marks_sheet['subject_3'] = subject_3
print("Subject Marks sheet in shorted order", subject_marks_sheet)

grade_marks_sheet = {}
for name in Marks_dataset.keys():
    grade_marks_sheet[name] = (np.sum(Marks_dataset.get(name))/300)*100

for percent in grade_marks_sheet.values():
    if percent > 90:
        print('A+')
    elif percent > 80 and percent <= 90:
        print('A')
    elif percent > 70 and percent <= 80:
        print('B+')
    elif percent > 60 and percent <= 70:
        print('B')
    elif percent > 50 and percent <= 60:
        print('C')
    elif percent <= 50:
        print('D')


