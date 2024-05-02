import sys
input = sys.stdin.readline

from collections import deque

m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

q = deque([])
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((j, i))

def isInBox(x, y):
    return 0 <= y < n and 0 <= x < m

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if isInBox(nx, ny) and box[ny][nx] == 0:
                q.append((nx, ny))
                box[ny][nx] = box[y][x] + 1
bfs()

result = 0

for row in box:
    if row.count(0) >= 1:
        print(-1)
        exit(0)

    result = max(result ,max(row))

print(result - 1)