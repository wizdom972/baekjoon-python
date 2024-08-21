from collections import deque

n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def next_year():
    to_sub = [[0] * m for _ in range(n)]
    is_melted = False

    for i in range(n):
        for j in range(m):
            if ice[i][j] > 0:
                ocean = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] == 0:
                        ocean += 1

                if ocean > 0:
                    is_melted = True
                    to_sub[i][j] = ocean

    if not is_melted:
        return False

    for i in range(n):
        for j in range(m):
            if to_sub[i][j]:
                ice[i][j] = max(0, ice[i][j] - to_sub[i][j])

    return True

def bfs(sx, sy, visited):
    visited[sx][sy] = True
    q = deque([(sx, sy)])

    while q:
        xx, yy = q.popleft()

        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if ice[nx][ny] > 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))

year = 0

while True:
    visited = [[False] * m for _ in range(n)]
    chunk = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and ice[i][j] > 0:
                bfs(i, j, visited)
                chunk += 1
                if chunk > 1:
                    print(year)
                    exit()

    if chunk == 0:
        print(0)
        break

    if not next_year():
        print(0)
        break

    year += 1
