basketNum, inputNum = map(int, input().split())
basketList = [0 for _ in range(basketNum)]

for i in range(inputNum):
    start, end, ballNum = map(int, input().split())
    for j in range(start - 1, end):
        basketList[j] = ballNum

print(*basketList)