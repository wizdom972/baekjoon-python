import sys

sys.setrecursionlimit(100000)


def find_parent(parent, x):
    while parent[x] != x:
        x = parent[x]

    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())

graph = []
for _ in range(e):
    a, b, c = map(int, input().split())

    graph.append((c, a, b))

graph.sort()

cost = 0
parent = [i for i in range(v + 1)]

for g in graph:
    c, a, b = g

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        cost += c

print(cost)
