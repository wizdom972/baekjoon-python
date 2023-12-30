list = []

for i in range(9):
    num = int(input())
    list.append(num)

sortedList = sorted(list, reverse=True)

maxNum = sortedList[0]

print(maxNum)
print((list.index(maxNum) + 1))