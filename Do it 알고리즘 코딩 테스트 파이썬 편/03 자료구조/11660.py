n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
sumGrid = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sumGrid[i][j] = sumGrid[i][j - 1] + sumGrid[i - 1][j] \
            + grid[i - 1][j - 1] - sumGrid[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sumGrid[x2][y2] - sumGrid[x2][y1 - 1] \
          - sumGrid[x1 - 1][y2] + sumGrid[x1 - 1][y1 - 1])