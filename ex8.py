sumMainDiagonal = 0

for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input(f"Enter the {j} number of the {i} row: ")))
        if i == j:
            sumMainDiagonal += row[j]
    print(row)

print(f"The sum of the main diagonal is: {sumMainDiagonal}")