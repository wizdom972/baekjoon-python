import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ice = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    if x < 0 or x > n - 1 or y < 0 or y > m - 1:
        return False
    
    if ice[x][y] == 0:
        ice[x][y] = 1

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True
    
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)