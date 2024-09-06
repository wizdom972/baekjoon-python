dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def spring_and_summer():
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree_list = tree[i][j]

                tree_list.sort()

                for index in range(len(tree_list)):
                    t = tree_list[index]

                    if nourish[i][j] >= t:
                        nourish[i][j] -= t
                        tree_list[index] += 1
                    else:

                        for d in tree_list[index:]:
                            nourish[i][j] += d // 2

                        tree[i][j] = tree_list[:index]

                        break


def fall():
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree_list = tree[i][j]

                for t in tree_list:
                    if t % 5 == 0:
                        for dir in range(8):
                            nx = i + dx[dir]
                            ny = j + dy[dir]

                            if 0 <= nx < n and 0 <= ny < n:
                                tree[nx][ny].append(1)


def winter():
    for i in range(n):
        for j in range(n):
            nourish[i][j] += to_be_added_nourish[i][j]


def pass_year():
    spring_and_summer()
    fall()
    winter()


n, m, k = map(int, input().split())
to_be_added_nourish = [list(map(int, input().split())) for _ in range(n)]

tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, age = map(int, input().split())

    tree[x - 1][y - 1].append(age)

nourish = [[5] * n for _ in range(n)]

for _ in range(k):
    pass_year()

tree_num = 0

for i in range(n):
    for j in range(n):
        if tree[i][j]:
            tree_num += len(tree[i][j])

print(tree_num)
