dataNum = int(input())

dataList = list(map(int, input().split()))

searchNum = int(input())

searched = 0

for i in dataList:
    if i == searchNum:
        searched += 1

print(searched)