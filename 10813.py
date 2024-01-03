basketNum, swapNum = map(int, input().split())
basketList = [i for i in range(basketNum + 1)]

for i in range(swapNum):
    first, second = map(int, input().split())
    basketList[first], basketList[second] = \
        basketList[second], basketList[first]

print(*basketList[1:])