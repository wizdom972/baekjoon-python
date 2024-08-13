import sys
input = sys.stdin.readline

n = int(input())

map = [[] for _ in range(n)]
for i in range(n):
    map[i] = list(input().strip())

maxCandy = 0

def calculateCandy(map):
    maxCandy = 0

    # 행 기준 사탕 세기
    for row in map:
        tempMax = 1

        for i in range(n-1):
            if row[i] != row[i+1]:
                if maxCandy < tempMax:
                    maxCandy = tempMax

                tempMax = 1
            else:
                tempMax += 1

                if i == n-2:
                    if maxCandy < tempMax:
                        maxCandy = tempMax

    # 열 기준 사탕 세기
    for j in range(n):
        tempMax = 1

        for i in range(n-1):
            if map[i][j] != map[i+1][j]:
                if maxCandy < tempMax:
                    maxCandy = tempMax

                tempMax = 1
            else:
                tempMax += 1

                if i == n-2:
                    if maxCandy < tempMax:
                        maxCandy = tempMax

    return maxCandy

for i in range(n):
    for j in range(n):
        # 좌우 변경
        if j + 1 < n and map[i][j] != map[i][j+1]:
            map[i][j], map[i][j+1] = map[i][j+1], map[i][j]

            candy = calculateCandy(map)
            if maxCandy < candy:
                maxCandy = candy

            # 원상 복구
            map[i][j], map[i][j+1] = map[i][j+1], map[i][j]

        # 상하 변경
        if i + 1 < n and map[i][j] != map[i+1][j]:
            map[i][j], map[i+1][j] = map[i+1][j], map[i][j]

            candy = calculateCandy(map)
            if maxCandy < candy:
                maxCandy = candy

            # 원상 복구
            map[i][j], map[i+1][j] = map[i+1][j], map[i][j]

print(maxCandy)
