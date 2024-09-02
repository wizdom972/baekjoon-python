code_sol = [
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1],
]


def find_code(barcode):
    result = []

    for row in barcode:
        end_index = -1

        if row.count(1):
            for i in range(m - 1, -1, -1):
                if row[i] == 1:
                    end_index = i
                    break

        if end_index != -1:
            result = row[i - 55 : i + 1]
            break

    return result


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    barcode = [[] for _ in range(n)]
    for i in range(n):
        barcode[i] = list(map(int, list(input())))

    code = find_code(barcode)

    resolved = []

    for i in range(0, 57, 7):
        bit = code[i : i + 7]
        for j in range(10):
            if bit == code_sol[j]:
                resolved.append(j)

    odd, even, sum_result = 0, 0, 0

    for i in range(0, 8, 2):
        odd += resolved[i]
        even += resolved[i + 1]

    sum_result = odd * 3 + even

    result = 0

    if sum_result % 10 == 0:
        result = sum(resolved)

    print(f"#{test_case} {result}")
