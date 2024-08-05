import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy, visited):
  visited[sx][sy] = True
  q = deque([(sx, sy)])
  area = 1


  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if not visited[nx][ny] and paper[nx][ny] == 1:
          q.append((nx, ny))
          visited[nx][ny] = True
          area += 1

  return area

drawingNum = 0
maxArea = 0

for i in range(n):
  for j in range(m):
    if paper[i][j] == 1 and not visited[i][j]:
      maxArea = max(maxArea, bfs(i, j, visited))
      drawingNum += 1

print(drawingNum)
print(maxArea)