def my_round(val):
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)

n = int(input())

if n <= 0:
    print(0)
else:
    level = [0] * n

    for i in range(n):
        level[i] = int(input())

    cut = my_round(n * 0.15)

    level.sort()
    print(my_round(sum(level[cut:n-cut]) / (n - 2 * cut)))