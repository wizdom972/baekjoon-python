import sys
input = sys.stdin.readline

n, k = map(int, input().split())

virus = []

land = [[] for _ in range(n)]
for i in range(n):
    land[i] = list(map(int, input().split()))

    for j in range(n):
        if land[i][j] != 0:
            virus.append((land[i][j], i, j, 0))

virus.sort()

s, x, y = map(int, input().split())

visited = [[False] * n for _ in range(n)]

from collections import deque

q = deque(virus)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virusNum, xx, yy, time = q.popleft()
    visited[xx][yy] = True

    if time == s:
        break

    for i in range(4):
        nx = xx + dx[i]
        ny = yy + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                land[nx][ny] = virusNum
                visited[nx][ny] = True
                q.append((virusNum, nx, ny, time + 1))

print(land[x-1][y-1])