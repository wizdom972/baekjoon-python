def cal_home_num(home_loc, k, x, y):
    count = 0

    for home in home_loc:
        h_x, h_y = home

        dist = abs(x - h_x) + abs(y - h_y)

        if dist < k:
            count += 1

    cost = k**2 + (k - 1) ** 2
    earn = count * m

    profit = earn - cost

    if profit < 0:
        return -1

    # print(x, y, k, profit, count)

    return count


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]

    home_loc = []
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                home_loc.append((i, j))

    max_home_num = 0

    for k in range(1, 2 * n + 1):
        for i in range(n):
            for j in range(n):
                temp_home_num = cal_home_num(home_loc, k, i, j)

                max_home_num = max(temp_home_num, max_home_num)

    print(f"#{test_case} {max_home_num}")
