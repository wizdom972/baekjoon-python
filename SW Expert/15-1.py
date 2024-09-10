T = int(input())
for test_case in range(1, T + 1):
    data = list(map(int, input().split()))

    n = data[0]

    data = data[1:]

    graph = [[] for _ in range(n)]
    for i in range(0, n * n, n):
        graph[i // n] = data[i : i + n]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][j] == 0:
                graph[i][j] = float("inf")

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # print(graph)

    cc = [0] * n
    for i in range(n):
        cc[i] = sum(graph[i])

    print(f"#{test_case} {min(cc)}")
