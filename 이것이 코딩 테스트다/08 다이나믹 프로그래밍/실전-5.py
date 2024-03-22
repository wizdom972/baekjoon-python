import sys
input = sys.stdin.readline

n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]

d = [10001] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(money[i], m + 1):
            d[j] = min(d[j], d[j - money[i]] + 1)

print(-1 if d[m] == 10001 else d[m])