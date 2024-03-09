positiveSum = 0
negativeCount = 0

for i in range(5):
    value = int(input("Enter a number: "))
    if value < 0:
        negativeCount += 1
    else:
        positiveSum += value

print("Sum of positive numbers:", positiveSum)
print("Count of negative numbers:", negativeCount)