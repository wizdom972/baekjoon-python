from collections import deque

for test_case in range(1, 11):
    n = int(input())

    start = (0, 0)
    end = (0, 0)

    maze = [[] for _ in range(16)]
    for i in range(16):
        maze[i] = list(map(int, input()))
        # print(maze[i])

        if maze[i].count(2):
            # print("asdf")
            start = (i, maze[i].index(2))

        elif maze[i].count(3):
            # print("sdfsdf")
            end = (i, maze[i].index(3))

    # print(start, end)

    visited = [[False] * 16 for _ in range(16)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def bfs(sx, sy, visited):
        visited[sx][sy] = True
        q = deque([(sx, sy)])

        while q:
            xx, yy = q.popleft()

            for j in range(4):
                nx = xx + dx[j]
                ny = yy + dy[j]

                if not visited[nx][ny] and maze[nx][ny] != 1:
                    if maze[nx][ny] == 3:
                        return 1
                    else:
                        q.append((nx, ny))
                        visited[nx][ny] = True

        return 0

    result = bfs(start[0], start[1], visited)

    print(f"#{n} {result}")