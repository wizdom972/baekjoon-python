n, m = map(int, input().split())

buckets = [[] for _ in range(n)]
for i in range(n):
    buckets[i] = list(map(int, input().split()))

move = []
for i in range(m):
    d, s = map(int, input().split())
    move.append((d, s))

cloud = [[False] * n for _ in range(n)]
cloud[n-1][0] = True
cloud[n-1][1] = True
cloud[n-2][0] = True
cloud[n-2][1] = True

dx = [0] + [0, -1, -1, -1, 0, 1, 1, 1]
dy = [0] + [-1, -1, 0, 1, 1, 1, 0, -1]

def move_cloud(d, s):
    global cloud
    new_cloud = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if cloud[i][j]:
                nx = (i + dx[d] * s) % n
                ny = (j + dy[d] * s) % n

                new_cloud[nx][ny] = True

    cloud = new_cloud

    for i in range(n):
        for j in range(n):
            if cloud[i][j]:
                buckets[i][j] += 1

def rain_dance():
    global cloud
    cross_x = [-1, -1, 1, 1]
    cross_y = [-1, 1, -1, 1]
    new_cloud = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if cloud[i][j]:
                count = 0

                for k in range(4):
                    nx = i + cross_x[k]
                    ny = j + cross_y[k]

                    if 0 <= nx < n and 0 <= ny < n and buckets[nx][ny]:
                        count += 1
                
                buckets[i][j] += count

    for i in range(n):
        for j in range(n):
            if buckets[i][j] >= 2 and not cloud[i][j]:
                new_cloud[i][j] = True
                buckets[i][j] -= 2

    cloud = new_cloud

for i in range(m):
    # print(f"***{i}번째 move***")

    d, s = move[i]
    # print(f"d: {d} s: {s}")

    # print("buckets")
    # for b in buckets:
    #     print(b)

    # print("before cloud:")
    # for c in cloud:
    #     print(c)

    move_cloud(d, s)

    # print("after cloud")
    # for c in cloud:
    #     print(c)

    rain_dance()

    # print("after rain dance buckets")
    # for b in buckets:
    #     print(b)

    # print("after rain dance cloud")
    # for c in cloud:
    #     print(c)


result = 0
for i in range(n):
    for j in range(n):
        result += buckets[i][j]

print(result)