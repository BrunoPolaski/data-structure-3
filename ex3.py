subjectOne = []
subjectTwo = []
subjectOneAvg = 0
subjectTwoAvg = 0

for i in range(6):
    subjectOne.append(int(input(f"Enter the {i} grade of subject 1 for student: ")))
    subjectTwo.append(int(input(f"Enter the {i} grade of subject 2 for student: ")))

print("Subject with the highest average:", 1 if sum(subjectOne) / 6 > sum(subjectTwo) / 6 else 2)