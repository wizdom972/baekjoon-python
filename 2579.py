import sys
input = sys.stdin.readline

n = int(input())

stair = []
for i in range(max(n, 3)):
    stair.append(int(input()))

d = [0] * max(n + 1, 4)
result = 0

d[1] = stair[0]
d[2] = stair[0] + stair[1]
d[3] = max(stair[1] + stair[2], stair[0] + stair[2])

for i in range(4, n + 1):
    d[i] = max(d[i-3] + stair[i-2] + stair[i-1], d[i-2] + stair[i-1])

print(d[-1])