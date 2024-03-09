numbers = []

for i in range(5):
    number = int(input("Enter a number: "))
    if number < 0:
        numbers.append(0)
    else:
        numbers.append(number)

print(numbers)