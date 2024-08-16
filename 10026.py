import sys
sys.setrecursionlimit(10**6)

n = int(input())

paint = [[] for _ in range(n)]
for i in range(n):
    paint[i] = list(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * n for _ in range(n)]
normalNum = 0

def dfs(sx, sy, color):
    visited[sx][sy] = True

    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if paint[nx][ny] == color:
                dfs(nx, ny, color)

    return

visited2 = [[False] * n for _ in range(n)]
redGreenNum = 0

def dfs2(sx, sy, color):
    visited2[sx][sy] = True

    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited2[nx][ny]:
            if color == 'R' or color == 'G':
                if paint[nx][ny] == "R" or paint[nx][ny] == "G":
                    dfs2(nx, ny, color)
            else:
                if paint[nx][ny] == color:
                    dfs2(nx, ny, color)

    return

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, paint[i][j])
            normalNum += 1
        if not visited2[i][j]:
            dfs2(i, j, paint[i][j])
            redGreenNum += 1

print(f"{normalNum} {redGreenNum}")