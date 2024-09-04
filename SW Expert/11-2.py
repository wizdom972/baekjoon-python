from collections import deque


def get_depth(tree, x, node, depth):
    if node == x:
        return depth

    for leaf in tree[node]:
        result = get_depth(tree, x, leaf, depth + 1)

        if result != -1:
            return result

    return -1


def find_co_ancestor(parent, a, b):
    a_depth = get_depth(tree, a, 1, 0)
    b_depth = get_depth(tree, b, 1, 0)

    if a_depth < b_depth:
        while a_depth < b_depth:
            b = parent[b]
            b_depth -= 1
    elif a_depth > b_depth:
        while a_depth > b_depth:
            a = parent[a]
            a_depth -= 1

    while a != b:
        a = parent[a]
        b = parent[b]

    return a


def count_tree(tree, sub_root):
    visited = [False] * (v + 1)
    count = 1

    visited[sub_root] = True
    q = deque([sub_root])

    while q:
        root = q.popleft()

        for node in tree[root]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
                count += 1

    return count


T = int(input())
for test_case in range(1, T + 1):
    v, e, a, b = map(int, input().split())

    parent = [i for i in range(v + 1)]
    tree = [[] for _ in range(v + 1)]

    data = list(map(int, input().split()))
    for i in range(0, len(data), 2):
        p, c = data[i], data[i + 1]

        tree[p].append(c)
        parent[c] = p

    sub_root = find_co_ancestor(parent, a, b)

    node_num = count_tree(tree, sub_root)

    print(f"#{test_case} {sub_root} {node_num}")
