import sys
input = sys.stdin.readline

n, m = map(int, input().split())

blocks = [[0] * m for _ in range(n)]
for i in range(n):
    blocks[i] = list(map(int, input().split()))

TOP = n * m
BOTTOM = n * m

LEFT = sum(blocks[i][0] for i in range(n))
for i in range(n):
    for j in range(m-1):
        if blocks[i][j] < blocks[i][j+1]:
            LEFT += (blocks[i][j+1] - blocks[i][j])

RIGHT = sum(blocks[i][-1] for i in range(n))
for i in range(n):
    for j in range(m-1, 0, -1):
        if blocks[i][j-1] > blocks[i][j]:
            RIGHT += (blocks[i][j-1] - blocks[i][j])

FRONT = sum(blocks[n-1])
for i in range(m):
    for j in range(n-1, 0, -1):
        if blocks[j][i] < blocks[j-1][i]:
            FRONT += (blocks[j-1][i] - blocks[j][i])

BACK = sum(blocks[0])
for i in range(m):
    for j in range(n-1):
        if blocks[j][i] < blocks[j+1][i]:
            BACK += (blocks[j+1][i] - blocks[j][i])

print(TOP + BOTTOM + LEFT + RIGHT + FRONT + BACK)