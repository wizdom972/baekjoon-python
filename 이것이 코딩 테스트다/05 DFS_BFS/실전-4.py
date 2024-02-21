import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append[(x, y)]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue

            if g[nx][ny] == 0:
                continue

            if g[nx][ny] == 1:
                g[nx][ny] = g[x][y] + 1
                queue.append((nx, ny))
    
    return g[n - 1][m - 1]

print(bfs(0, 0))