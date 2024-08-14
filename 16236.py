import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = []
shark_x, shark_y = 0, 0

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 9:
            shark_x, shark_y = i, j
            line[j] = 0
    board.append(line)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(sx, sy, size):
    visited = [[False] * n for _ in range(n)]
    q = deque([(sx, sy, 0)])
    visited[sx][sy] = True
    fish_list = []

    while q:
        x, y, dist = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] <= size:
                    visited[nx][ny] = True
                    if 0 < board[nx][ny] < size:
                        fish_list.append((dist + 1, nx, ny))
                    else:
                        q.append((nx, ny, dist + 1))
    
    if fish_list:
        fish_list.sort()
        return fish_list[0]
    else:
        return None

size = 2
to_next_size = 2
time = 0

while True:
    result = bfs(shark_x, shark_y, size)
    
    if result is None:
        break
    
    dist, fish_x, fish_y = result

    time += dist
    board[fish_x][fish_y] = 0
    shark_x, shark_y = fish_x, fish_y

    to_next_size -= 1
    if to_next_size == 0:
        size += 1
        to_next_size = size

print(time)
