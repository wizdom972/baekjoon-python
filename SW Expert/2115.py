def get_max_profit(arr):
    n = len(arr)
    max_square_sum = 0

    def backtrack(index, cur_sum, cur_square_sum):
        nonlocal max_square_sum

        if cur_sum > c:
            return

        max_square_sum = max(max_square_sum, cur_square_sum)

        for i in range(index, n):
            backtrack(i + 1, cur_sum + arr[i], cur_square_sum + arr[i] ** 2)
            backtrack(i + 1, cur_sum, cur_square_sum)

    backtrack(0, 0, 0)

    return max_square_sum


def take_honey(g1, g2, c):
    # print(g1, g2, c)

    profit = 0

    for g in (g1, g2):
        honey_val = []

        for x, y in g:
            honey_val.append(honey[x][y])

        honey_val.sort(reverse=True)
        # print(honey_val)

        profit += get_max_profit(honey_val)

        # print(profit)

    # print(profit)

    return profit


T = int(input())
for test_case in range(1, T + 1):
    n, m, c = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(n)]

    group = []
    for i in range(n):
        for j in range(n - m + 1):
            g = []

            for k in range(m):
                g.append((i, j + k))

            group.append(g)

    max_profit = 0

    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            g1 = group[i]
            g2 = group[j]

            if not set(g1) & set(g2):
                temp_profit = take_honey(g1, g2, c)

                if temp_profit > max_profit:
                    max_profit = temp_profit

    print(f"#{test_case} {max_profit}")
