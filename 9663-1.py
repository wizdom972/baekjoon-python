n = int(input())
count = 0

row = [0] * n
col = [0] * n
digonal_1 = [0] * (2 * n - 1)
digoanl_2 = [0] * (2 * n - 1)


def n_queen(x):
    global count

    if x == n:
        count += 1
        return

    else:
        for i in range(n):
            if col[i] or digonal_1[x + i] or digoanl_2[x - i + n - 1]:
                continue

            else:
                row[x] = 1
                col[i] = 1
                digonal_1[x + i] = 1
                digoanl_2[x - i + n - 1] = 1

                n_queen(x + 1)

                row[x] = 0
                col[i] = 0
                digonal_1[x + i] = 0
                digoanl_2[x - i + n - 1] = 0


n_queen(0)
print(count)
