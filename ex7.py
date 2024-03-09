matrix = []

for i in range(5):
    for j in range(5):
        number = int(input(f"Enter the {j} number of the {i} row: "))
        matrix += (number)

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i] == matrix[j]:
            print(f"Number {matrix[i]} is repeated at position {i} and {j}")
            break