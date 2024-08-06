for _ in range(1, 11):
    n = int(input())

    ladder = [[0] * 100 for _ in range(100)]
    for i in range(100):
        ladder[i] = list(map(int, input().split()))

    curY = ladder[-1].index(2)

    for i in range(99, -1, -1):
        if curY > 0:
            if ladder[i][curY - 1] == 1:
                while curY > 0 and ladder[i][curY - 1] == 1:
                    curY -= 1
                continue

        if curY < 99:
            if ladder[i][curY + 1] == 1:
                while curY < 99 and ladder[i][curY + 1] == 1:
                    curY += 1
                continue

        else:
            continue

    print(f"#{n} {curY}")
