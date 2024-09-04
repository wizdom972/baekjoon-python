from itertools import permutations

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    data = list(map(int, input().split()))

    office = (data[0], data[1])
    home = (data[2], data[3])

    customer = []
    for i in range(4, len(data), 2):
        loc = (data[i], data[i + 1])

        customer.append(loc)

    min_dist = int(1e9)

    for perm in permutations(range(n), n):
        temp_dist = 0

        # 회사에서 첫번째 고객
        dist = abs(office[0] - customer[perm[0]][0]) + abs(
            office[1] - customer[perm[0]][1]
        )
        temp_dist += dist

        # 첫번째 고객 ~ 마지막 고객
        for i in range(n - 1):
            dist = abs(customer[perm[i]][0] - customer[perm[i + 1]][0]) + abs(
                customer[perm[i]][1] - customer[perm[i + 1]][1]
            )
            temp_dist += dist

        # 마지막 고객에서 집
        dist = abs(customer[perm[n - 1]][0] - home[0]) + abs(
            customer[perm[n - 1]][1] - home[1]
        )
        temp_dist += dist

        if temp_dist < min_dist:
            min_dist = temp_dist

    print(f"#{test_case} {min_dist}")
