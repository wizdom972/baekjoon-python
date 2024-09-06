from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    k = int(input())
    s_list = list(input())

    n = len(s_list)

    parts = []
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            parts.append("".join(s_list[j : j + i]))

    parts = list(set(parts))
    parts.sort()

    if len(parts) < k:
        print(f"#{test_case} none")
        continue
    else:
        print(f"#{test_case} {parts[k-1]}")
