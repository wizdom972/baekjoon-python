import sys
input = sys.stdin.readline

n, k = map(int, input().split())

d = [[0] * max(3, n+1) for _ in range(max(3, k+1))]

for i in range(1, n+1):
    d[1][i] = 1
    d[2][i] = i + 1

for i in range(3, k+1):
    d[i][1] = i
    for j in range(2, n+1):
        d[i][j] = (d[i-1][j] + d[i][j-1]) % int(1e9)

print(d[k][n])