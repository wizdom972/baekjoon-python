def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    parent = [i for i in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())

        union_parent(parent, a, b)

    for i in range(n + 1):
        parent[i] = find_parent(parent, i)

    parent = parent[1:]

    print(f"#{test_case} {len(set(parent))}")
