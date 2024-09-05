import math


def get_cost(a, b):
    a_x = island_x[a]
    a_y = island_y[a]

    b_x = island_x[b]
    b_y = island_y[b]

    dist = (a_x - b_x) ** 2 + (a_y - b_y) ** 2
    cost = e * dist

    return cost


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def round_fix(num):
    sub = num - int(num)

    if sub >= 0.5:
        return int(num) + 1
    else:
        return int(num)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))

    e = float(input())

    dist = []
    for i in range(n):
        for j in range(i + 1, n):
            dist.append((get_cost(i, j), i, j))

    dist.sort()

    parent = [i for i in range(n)]
    cost_sum = 0

    for edge in dist:
        cost, a, b = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union(parent, a, b)
            cost_sum += cost

    print(f"#{test_case} {round_fix(cost_sum)}")
