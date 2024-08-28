import copy

n, m = map(int, input().split())

office = [[] for _ in range(n)]
for i in range(n):
    office[i] = list(map(int, input().split()))

cctvs = []
for i in range(n):
    for j in range(m):
        if 1 <= office[i][j] <= 5:
            cctvs.append((i, j, office[i][j]))

# 방향 설정
directions = {
    1: [[(0, 1)], [(0, -1)], [(-1, 0)], [(1, 0)]],
    2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
    3: [[(0, 1), (-1, 0)], [(-1, 0), (0, -1)], [(0, -1), (1, 0)], [(1, 0), (0, 1)]],
    4: [[(0, 1), (-1, 0), (0, -1)], [(-1, 0), (0, -1), (1, 0)], 
        [(0, -1), (1, 0), (0, 1)], [(1, 0), (0, 1), (0, -1)]],
    5: [[(0, 1), (0, -1), (-1, 0), (1, 0)]]
}

def fill(board, dirs, x, y):
    for dir in dirs:
        for dx, dy in dir:
            nx, ny = x, y

            while True:
                nx += dx
                ny += dy

                if not (0 <= nx < n and 0 <= ny < m):
                    break
                
                if board[nx][ny] == 6:
                    break
                
                if board[nx][ny] == 0:
                    board[nx][ny] = "#"

def dfs(depth, office):
    global min_blind_place
    
    if depth == len(cctvs):
        blind_place = sum(row.count(0) for row in office)
        min_blind_place = min(min_blind_place, blind_place)
        return
    
    x, y, cctv_type = cctvs[depth]
    temp_office = copy.deepcopy(office)

    for direction in directions[cctv_type]:
        fill(temp_office, [direction], x, y)
        dfs(depth+1, temp_office)
        temp_office = copy.deepcopy(office)

min_blind_place = int(1e9)
dfs(0, office)

print(min_blind_place)