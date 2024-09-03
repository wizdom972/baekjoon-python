from collections import deque

n, m = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(sx, sy):
    visited[sx][sy] = True
    q = deque([(sx, sy)])

    while q:
        xx, yy = q.popleft()

        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if cheeze[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = True


def melt(visited):
    global cheeze

    new_cheeze = [[] for _ in range(n)]
    for i in range(n):
        new_cheeze[i] = cheeze[i][:]

    for i in range(n):
        for j in range(m):
            if cheeze[i][j] == 1:
                count = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < m:
                        if visited[nx][ny]:
                            count += 1

                if count >= 2:
                    new_cheeze[i][j] = 0

    cheeze = new_cheeze


def count_cheeze():
    global cheeze

    return sum([sum(row) for row in cheeze])


cheeze_num = count_cheeze()
time = 0

while cheeze_num > 0:
    visited = [[False] * m for _ in range(n)]

    bfs(0, 0)
    melt(visited)

    cheeze_num = count_cheeze()
    time += 1

print(time)
