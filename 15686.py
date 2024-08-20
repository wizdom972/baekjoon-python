from itertools import combinations

n, m = map(int, input().split())

board = [[] for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))

chicken = []
home = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken.append((i, j))
        elif board[i][j] == 1:
            home.append((i, j))

def chicken_dist(combi):
    chickDist = 0
    
    for h in home:
        min_dist = int(1e9)
        h_x = h[0]
        h_y = h[1]

        for c in combi:
            c_x = chicken[c][0]
            c_y = chicken[c][1]

            temp_dist = abs(c_x - h_x) + abs(c_y - h_y)
            min_dist = min(min_dist, temp_dist)

        chickDist += min_dist

    return chickDist
        
result = int(1e9)

for combi in combinations(range(len(chicken)), m):
    dist = chicken_dist(combi)

    result = min(result, dist)

print(result)