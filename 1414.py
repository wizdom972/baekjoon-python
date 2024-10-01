def find_parent(parent, x):
    while parent[x] != x:
        x = parent[x]

    return x


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def char_to_len(char):
    if char.isupper():
        return (ord(char) - ord("A") + 27)
    elif char.islower():
        return (ord(char) - ord("a") + 1)
    else:
        return 0

n = int(input())

graph = []
for _ in range(n):
    row = list(input())

    length = []
    for c in row:
        length.append(char_to_len(c))

    graph.append(length)

weights = []
for i in range(n):
    for j in range(n):
        weight = graph[i][j]

        if weight != 0:
            weights.append((weight, i, j))

weights.sort()

count = 0
parent = [i for i in range(n)]
line_len = sum([sum(row) for row in graph])

for w in weights:
    weight, a, b = w

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        count += 1
        line_len -= weight

        if count >= n - 1:
            break

if count >= n - 1:
    print(line_len)
else:
    print(-1)