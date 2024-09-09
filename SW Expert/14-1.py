def find_matrix(sx, sy):
    origin_x = sx
    origin_y = sy

    visited[sx][sy] = True

    while sy < n and data[sx][sy] != 0:
        sy += 1

    while sx < n and data[sx][origin_y] != 0:
        sx += 1

    for i in range(origin_x, sx):
        for j in range(origin_y, sy):
            visited[i][j] = True

    x = sx - origin_x
    y = sy - origin_y

    return (x * y, x, y)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    visited = [[False] * n for _ in range(n)]

    matrix = []

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and data[i][j] != 0:
                matrix.append(find_matrix(i, j))

    matrix.sort()

    print(f"#{test_case} {len(matrix)} ", end="")
    for m in matrix:
        area, x, y = m

        print(f"{x} {y} ", end="")
    print()
