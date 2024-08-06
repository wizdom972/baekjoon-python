for _ in range(10):
    n = int(input())

    matrix = [[0] * 100 for _ in range(100)]
    for i in range(100):
        matrix[i] = list(map(int, input().split()))

    result = int(-1e9)

    for i in range(100):
        result = max(result, sum(matrix[i]))

    for i in range(100):
        colSum = 0

        for j in range(100):
            colSum += matrix[j][i]

        result = max(result, colSum)

    for i in range(100):
        crossSum1 = 0
        crossSum1 += matrix[i][i]

        crossSum2 = 0
        crossSum2 += matrix[i][99-i]

        result = max(crossSum1, crossSum2, result)

    print(f"#{n} {result}")