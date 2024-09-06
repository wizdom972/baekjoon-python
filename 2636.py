from collections import deque

n, m = map(int, input().split())

cheeze = [[] for _ in range(n)]
for i in range(n):
    cheeze[i] = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def outside_air(cheeze, sx, sy, visited):
    visited[sx][sy] = True
    q = deque([(sx, sy)])

    while q:
        xx, yy = q.popleft()

        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if cheeze[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))

def count_cheeze(cheeze):
    return sum([sum(row) for row in cheeze])

def melt(visited):
    global cheeze

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < m and cheeze[nx][ny] == 1:
                        cheeze[nx][ny] = 0

cheeze_cnt = []
time = 0

while True:
    # print(f"***time :{time} ***")

    cnt = count_cheeze(cheeze)
    # print(f"cnt: {cnt}")
    if cnt > 0:
        cheeze_cnt.append(cnt)
    else:
        break

    # for c in cheeze:
    #     print(c)

    # print("<<after melt>>")

    visited = [[False] * m for _ in range(n)]
    outside_air(cheeze, 0, 0, visited)
    melt(visited)

    # for c in cheeze:
    #     print(c)

    time += 1

print(time)
print(cheeze_cnt[-1])

