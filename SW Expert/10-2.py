def binary_search(left, right, left_index):
    while right - left > 1e-12:
        mid = (left + right) / 2

        left_force = 0
        for i in range(left_index + 1):
            dist = (mid - loc[i]) ** 2
            left_force += weight[i] / dist

        right_force = 0
        for i in range(left_index + 1, n):
            dist = (loc[i] - mid) ** 2
            right_force += weight[i] / dist

        if left_force < right_force:
            right = mid
        elif left_force > right_force:
            left = mid
        else:
            break
    return (left + right) / 2


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    data = list(map(int, input().split()))

    loc = data[:n]
    weight = data[n:]

    result = [0] * (n - 1)

    for i in range(n - 1):
        left = loc[i]
        right = loc[i + 1]
        result[i] = binary_search(left, right, i)

    sol = " ".join(f"{x:.10f}" for x in result)
    print(f"#{test_case} {sol}")
