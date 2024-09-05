n = int(input())

result = 0
row = [0] * n


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[i] - row[x]) == abs(i - x):
            return False

    return True


def n_queen(x):
    global result

    if x == n:
        result += 1
        return
    else:
        for i in range(n):
            row[x] = i

            if is_promising(x):
                n_queen(x + 1)


n_queen(0)
print(result)
