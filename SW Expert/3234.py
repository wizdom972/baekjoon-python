from itertools import permutations


def backtrack(perm, left_weight, right_weight, index):
    global count, n

    if left_weight > total_weight // 2:
        remain = n - index
        count += 2**remain

        return

    if index == n:
        if left_weight >= right_weight:
            count += 1

        return

    backtrack(perm, left_weight + perm[index], right_weight, index + 1)

    if right_weight + perm[index] <= left_weight:
        backtrack(perm, left_weight, right_weight + perm[index], index + 1)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    weights = list(map(int, input().split()))

    count = 0
    total_weight = sum(weights)

    for perm in permutations(weights, n):
        backtrack(perm, 0, 0, 0)

    print(f"#{test_case} {count}")
