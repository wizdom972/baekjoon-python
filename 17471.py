from collections import deque
from itertools import combinations


def bfs(x, g, visited):
    visited[x] = True
    q = deque([x])

    while q:
        a = q.popleft()

        for node in graph[a]:
            if not visited[node] and node in g:
                q.append(node)
                visited[node] = True


n = int(input())
population = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for i in range(n):
    edge_num, *nodes = list(map(int, input().split()))

    graph[i + 1] = nodes

min_diff = int(1e12)
can_be_divided = False

for i in range(1, n // 2 + 1):
    for g1 in combinations(range(1, n + 1), i):
        g2 = set(range(1, n + 1)) - set(g1)
        g2 = list(g2)

        v1 = [False] * (n + 1)
        v2 = [False] * (n + 1)

        bfs(g1[0], g1, v1)
        bfs(g2[0], g2, v2)

        flag_1 = False
        for node in g1:
            if not v1[node]:
                flag_1 = True
                break

        if flag_1:
            continue

        flag_2 = False
        for node in g2:
            if not v2[node]:
                flag_2 = True
                break

        if flag_2:
            continue

        can_be_divided = True

        temp_diff = abs(
            sum([population[n1] for n1 in g1]) - sum([population[n2] for n2 in g2])
        )

        min_diff = min(min_diff, temp_diff)

if can_be_divided:
    print(min_diff)
else:
    print(-1)
