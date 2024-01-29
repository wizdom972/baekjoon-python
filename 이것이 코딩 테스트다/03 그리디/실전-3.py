n, m = map(int, input().split())
card = [list(map(int, input().split())) for _ in range(n)]
maxNum = 0

for i in range(n):
    if maxNum < min(card[i]):
        maxNum = min(card[i])

print(maxNum)