from collections import deque

n, l, r = map(int, input().split())

map_list = [[] for _ in range(n)]
for i in range(n):
    map_list[i] = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy, visited):
    visited[sx][sy] = True
    q = deque([(sx, sy)])
    union = [(map_list[sx][sy], sx, sy)]

    while q:
        xx, yy = q.popleft()
        cur_pop = map_list[xx][yy]

        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                new_pop = map_list[nx][ny]

                if l <= abs(new_pop - cur_pop) <= r:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    union.append((new_pop, nx, ny))

    pop_sum = 0
    for contry in union:
        pop_sum += contry[0]

    pop_sum = pop_sum // len(union)

    for contry in union:
        c_x = contry[1]
        c_y = contry[2]

        map_list[c_x][c_y] = pop_sum

day = 0

while True:
    count = 0
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                count += 1
                bfs(i, j, visited)

    if count == n*n:
        print(day)
        break

    day += 1