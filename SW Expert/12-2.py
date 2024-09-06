import heapq

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

INF = int(1e9)


def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))

    cost[0][0] = 0

    while q:
        cur_cost, x, y = heapq.heappop(q)

        if cur_cost > cost[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cur_cost + grid[nx][ny]

                if new_cost < cost[nx][ny]:
                    cost[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    grid = [list(map(int, list(input()))) for _ in range(n)]

    cost = [[INF] * n for _ in range(n)]

    dijkstra()

    print(f"#{test_case} {cost[n-1][n-1]}")
