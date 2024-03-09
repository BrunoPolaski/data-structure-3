matrix = []
allEven = True

for i in range(3):
    row = []
    for j in range(3):
        row += int(input(f"Enter the {j} number of the {i} row: "))
        if row[j] % 2 != 0:
            allEven = False
    matrix += row

print(allEven)