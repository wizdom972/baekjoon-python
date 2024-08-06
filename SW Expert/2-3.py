for test_case in range(1, 11):
    n = int(input())
    
    table = [[0] * 100 for _ in range(100)]
    for i in range(100):
        table[i] = list(map(int, input().split()))

    for _ in range(100):
        for j in range(100):
            for i in range(100):
                current = table[i][j]

                if current == 1:
                    if i + 1 < 100 and table[i+1][j] == 0:
                        table[i+1][j] = 1
                        table[i][j] = 0
                    elif i == 99:
                        table[i][j] = 0
                elif current == 2:
                    if i - 1 >= 0 and table[i-1][j] == 0:
                        table[i-1][j] = 2
                        table[i][j] = 0
                    elif i == 0:
                        table[i][j] = 0

    count = 0

    for j in range(100):
        stuck = False

        for i in range(100):
            if table[i][j] == 1:
                stuck = True
            elif table[i][j] == 2 and stuck:
                count += 1
                stuck = False

    print(f"#{test_case} {count}")