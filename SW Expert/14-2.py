from collections import deque


def bfs(x, visited):
    visited[x] = True
    q = deque([(1, x, [x])])
    max_dist = [x]

    while q:
        dist, node, route = q.popleft()

        if dist > len(max_dist):
            max_dist = route

        for nx in graph[node]:
            route.append(nx)
            q.append((dist + 1, nx, route))
            visited[nx] = True

    return max_dist


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    data = list(map(int, input().split()))

    screw = [(0, 0) for _ in range(n)]
    for i in range(0, 2 * n, 2):
        screw[i // 2] = (data[i], data[i + 1])

    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s_e = screw[i][1]
            s_s = screw[j][0]

            if s_e == s_s:
                graph[i].append(j)

    max_len = []

    for i in range(n):
        visited = [False] * n
        temp_max = bfs(i, visited)

        if len(temp_max) > len(max_len):
            max_len = temp_max

    print(f"#{test_case} ", end="")
    for index in max_len:
        print(f"{screw[index][0]} {screw[index][1]} ", end="")
    print()
