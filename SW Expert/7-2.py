T = int(input())
for test_case in range(1, T+1):
    day, month, threeMonth, year = map(int, input().split())
    usePlan = list(map(int, input().split()))
    usePlan = [0] + usePlan

    d = [int(1e9)] * 13
    d[0] = 0

    for i in range(1, 13):
        if i > 2:
            d[i] = min(
                d[i-1] + day * usePlan[i],
                d[i-1] + month,
                d[i-3] + threeMonth
            )
        else:
            d[i] = min(
                d[i-1] + day * usePlan[i],
                d[i-1] + month
            )

    result = min(d[12], year)

    # print(d)

    print(f"#{test_case} {result}")

