from collections import deque

for test_case in range(1, 11):
    datalen, start = map(int, input().split())
    edges = list(map(int, input().split()))

    graph = [[] for _ in range(101)]
    for i in range(0, datalen, 2):
        if edges[i+1] not in graph[edges[i]]:
            graph[edges[i]].append(edges[i+1])

    # print("*******graph*******")
    # for g in graph:
    #     print(g)
    # print("*******graph*******")

    visited = [False] * (101)
    depth = [-1] * (101)
    

    def dfs(start, visited, depth):
        visited[start] = True
        q = deque([start])

        while q:
            node = q.popleft()

            for g in graph[node]:
                if not visited[g]:
                    q.append(g)
                    visited[g] = True
                    depth[g] = depth[node] + 1


    dfs(start, visited, depth)
    maxDepth = max(depth)

    resultList = list(filter(lambda i: depth[i] == maxDepth, range(len(depth))))
    print(f"#{test_case} {resultList[-1]}")