import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mapList = [list(map(int, input().split())) for _ in range(n)]

tempMap = [[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if tempMap[nx][ny] == 0:
                tempMap[nx][ny] = 2
                virus(nx, ny)

def safeZone():
    count = 0

    for i in range(n):
        for j in range(m):
            if tempMap[i][j] == 0:
                count += 1
    return count

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                tempMap[i][j] = mapList[i][j]

        for i in range(n):
            for j in range(m):
                if tempMap[i][j] == 2:
                    virus(i, j)
        
        result = max(result, safeZone())
        return
    
    for i in range(n):
        for j in range(m):
            if mapList[i][j] == 0:
                mapList[i][j] = 1
                count += 1
                dfs(count)
                mapList[i][j] = 0
                count -= 1

dfs(0)
print(result)