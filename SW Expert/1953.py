from collections import deque


def bfs(sx, sy, t_type, time):
    visited = [[False] * m for _ in range(n)]
    visited[sx][sy] = True

    q = deque([(sx, sy, t_type, time)])
    cnt = 1

    while q:
        x, y, t_type, time = q.popleft()

        if time >= l:
            continue

        for dx, dy in turnel[t_type]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if (
                    under_ground[nx][ny] > 0
                    and under_ground[nx][ny] in can_be_connected[(dx, dy)]
                ):
                    visited[nx][ny] = True
                    cnt += 1
                    q.append((nx, ny, under_ground[nx][ny], time + 1))

    return cnt


turnel = {
    1: [(0, 1), (1, 0), (-1, 0), (0, -1)],
    2: [(-1, 0), (1, 0)],
    3: [(0, 1), (0, -1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(0, -1), (1, 0)],
    7: [(-1, 0), (0, -1)],
}

can_be_connected = {
    (1, 0): [1, 2, 4, 7],
    (-1, 0): [1, 2, 5, 6],
    (0, 1): [1, 3, 6, 7],
    (0, -1): [1, 3, 4, 5],
}

T = int(input())
for test_case in range(1, T + 1):
    n, m, r, c, l = map(int, input().split())

    under_ground = [[] for _ in range(n)]
    for i in range(n):
        under_ground[i] = list(map(int, input().split()))

    result = bfs(r, c, under_ground[r][c], 1)

    print(f"#{test_case} {result}")
