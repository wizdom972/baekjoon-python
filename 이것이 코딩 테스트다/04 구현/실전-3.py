n, m = map(int, input().split())
x, y, d = map(int, input().split())
mapGrid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[x][y] = 1
count = 1
turnTime = 0

direction = [
    (-1, 0),    #north
    (0, 1),     #east
    (1, 0),     #south
    (0, -1)     #west    
    ]

while True:
    left = d - 1 if d > 0 else 3
    nx = x + direction[left][0]
    ny = y + direction[left][1]

    if visited[nx][ny] == 0 and mapGrid[nx][ny] == 0:
        d = left
        x = nx
        y = ny
        visited[nx][ny] = 1
        count += 1
        turnTime = 0
        continue
    else:
        d = left
        turnTime += 1

    if turnTime == 4:
        nx = x - direction[d][0]
        ny = y - direction[d][1]

        if mapGrid[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny
            turnTime = 0
            continue

print(count)

