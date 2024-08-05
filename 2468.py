import sys
input = sys.stdin.readline

from collections import deque

n = int(input())

height = [[0] * n for _ in range(n)]
maxNum = -1
for i in range(n):
    height[i] = list(map(int, input().split()))
    maxNum = max(maxNum, max(height[i]))

def bfs(x, y, h, visited):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        xx, yy = q.popleft()

        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and height[nx][ny] > h:
                    q.append((nx, ny))
                    visited[nx][ny] = True

result = 0
for i in range(maxNum):
    visited = [[False] * n for _ in range(n)]
    count = 0

    for j in range(n):
        for k in range(n):
            if height[j][k] > i and not visited[j][k]:
                bfs(j, k, i, visited)
                count += 1

    result = max(result, count)

print(result)