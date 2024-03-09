list = []
for i in range(4):
    list += int(input("Enter a number: "))

for i in range(4):
    for j in range(4):
        if list[i] < list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp

print(list)