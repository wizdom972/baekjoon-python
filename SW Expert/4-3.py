from collections import deque

for test_case in range(1, 11):
    v, e = map(int, input().split())
    edges = list(map(int, input().split()))

    graph = [[] for _ in range(v+1)]
    for i in range(0, len(edges), 2):
        vNum = edges[i]
        connected = edges[i+1]

        graph[vNum].append(connected)

    visited = [False] * (v+1)
    stack = deque([])

    def dfs(sv):
        visited[sv] = True

        for g in graph[sv]:
            if not visited[g]:
                dfs(g)

        stack.append(sv)

    for i in range(1, v+1):
        if not visited[i]:
            dfs(i)

    result = list(map(str, stack))
    result.reverse()
    result = " ".join(result)

    print(f"#{test_case} {result}")