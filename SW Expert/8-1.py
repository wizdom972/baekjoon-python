dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(sx, sy, visited, dist):
    global maxDistance, start

    if dist[sx][sy]:
        return dist[sx][sy]
    
    tempMax = 1

    visited[sx][sy] = True

    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and rooms[nx][ny] == rooms[sx][sy] + 1:
                tempMax = max(tempMax, dfs(nx, ny, visited, dist) + 1)

    visited[sx][sy] = False

    dist[sx][sy] = tempMax

    return dist[sx][sy]

T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    rooms = [[] for _ in range(n)]
    for i in range(n):
        rooms[i] = list(map(int, input().split()))

    visited = [[False] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    maxDistance = 1
    start = n*n + 1

    for i in range(n):
        for j in range(n):
            temp = dfs(i, j, visited, dist)

            if temp > maxDistance or (temp == maxDistance and start > rooms[i][j]):
                maxDistance = temp
                start = rooms[i][j]

    print(f"#{test_case} {start} {maxDistance}")