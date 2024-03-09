matrix = []
highestAvg = 0

for i in range(3):
    row = []
    for j in range(3):
        row += int(input(f"Enter the {j} grade of the {i} student: "))
    matrix += row

for i in range(3):
    avg = sum(matrix[i]) / 3
    if i == 0 or avg > highestAvg:
        highestAvg = avg
        highestStudent = i

print("The student with the highest average is student", highestStudent + 1, "with an average of", highestAvg)