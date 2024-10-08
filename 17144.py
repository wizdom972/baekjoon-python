def spread_dust():
    global dust

    new_dust = [[0] * c for _ in range(r)]
    new_dust[air_cleaner_loc[0]][0] = -1
    new_dust[air_cleaner_loc[1]][0] = -1

    for i in range(r):
        for j in range(c):
            if dust[i][j] > 0:
                cnt = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < r and 0 <= ny < c and dust[nx][ny] != -1:
                        cnt += 1
                        new_dust[nx][ny] += dust[i][j] // 5

                new_dust[i][j] += dust[i][j] - (dust[i][j] // 5) * cnt

    dust = new_dust


def clean_air():
    # 위쪽 공기청정기 반시계 방향 순환
    up_x, up_y = air_cleaner_loc[0], 0

    # 아래 -> 위
    for i in range(up_x - 1, 0, -1):
        dust[i][0] = dust[i - 1][0]
    # 왼쪽 -> 오른쪽
    for i in range(c - 1):
        dust[0][i] = dust[0][i + 1]
    # 위 -> 아래
    for i in range(up_x):
        dust[i][c - 1] = dust[i + 1][c - 1]
    # 오른쪽 -> 왼쪽
    for i in range(c - 1, 1, -1):
        dust[up_x][i] = dust[up_x][i - 1]
    dust[up_x][1] = 0

    # 아래쪽 공기청정기 시계 방향 순환
    down_x, down_y = air_cleaner_loc[1], 0

    # 위 -> 아래
    for i in range(down_x + 1, r - 1):
        dust[i][0] = dust[i + 1][0]
    # 왼쪽 -> 오른쪽
    for i in range(c - 1):
        dust[r - 1][i] = dust[r - 1][i + 1]
    # 아래 -> 위
    for i in range(r - 1, down_x, -1):
        dust[i][c - 1] = dust[i - 1][c - 1]
    # 오른쪽 -> 왼쪽
    for i in range(c - 1, 1, -1):
        dust[down_x][i] = dust[down_x][i - 1]
    dust[down_x][1] = 0


r, c, t = map(int, input().split())

dust = [[] for _ in range(r)]
for i in range(r):
    dust[i] = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

air_cleaner_loc = []
for i in range(r):
    if dust[i][0] == -1:
        air_cleaner_loc.append(i)

for _ in range(t):
    spread_dust()
    clean_air()

result = sum([sum(row) for row in dust]) + 2
print(result)
