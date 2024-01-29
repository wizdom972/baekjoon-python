n, m = map(int, input().split())
card = [list(map(int, input().split())) for _ in range(n)]
#maxRow = 0
maxNum = 0

for i in range(n):
    if maxNum < min(card[i]):
        #maxRow = i
        maxNum = min(card[i])

print(maxNum)