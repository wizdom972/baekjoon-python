dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(sx, sy, visited, isGongsa, dist, curH):
    global maxDistance
    maxDistance = max(maxDistance, dist)

    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True

            if mount[nx][ny] < curH:
                dfs(nx, ny, visited, isGongsa, dist + 1, mount[nx][ny])
            elif not isGongsa and mount[nx][ny] - k < curH:
                dfs(nx, ny, visited, True, dist + 1, curH - 1)

            visited[nx][ny] = False

    visited[sx][sy] = False

T = int(input())
for test_case in range(1, T+1):
    n, k = map(int, input().split())

    maxHeight = 0

    mount = [[] for _ in range(n)]
    for i in range(n):
        mount[i] = list(map(int, input().split()))

        tempMax = max(mount[i])
        if tempMax > maxHeight:
            maxHeight = tempMax

    maxDistance = 0
    visited = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if mount[i][j] == maxHeight:
                visited[i][j] = True
                dfs(i, j, visited, False, 1, maxHeight)
                visited[i][j] = False

    print(f"#{test_case} {maxDistance}")