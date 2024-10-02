from collections import deque

def topological_sort(graph, in_degree, n):
    result = []
    q = deque([])

    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        result.append(node)

        for next_node in graph[node]:
            in_degree[next_node] -= 1

            if in_degree[next_node] == 0:
                q.append(next_node)

    if len(result) == n:
        return result
    else:
        return [0]

n, m = map(int, input().split())

orders = []
for _ in range(m):
    s_num, *order = list(map(int, input().split()))
    orders.append(order)

graph = [[] for _ in range(n+1)]
in_degree = [0] * (n + 1)

for order in orders:
    length = len(order)

    for i in range(length - 1):
        graph[order[i]].append(order[i+1])
        in_degree[order[i+1]] += 1

# print(graph, in_degree)

answer = topological_sort(graph, in_degree, n)

if answer == [0]:
    print(0)
else:
    for a in answer:
        print(a)