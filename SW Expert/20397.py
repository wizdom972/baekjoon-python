T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    stones = list(map(int, input().split()))

    for i in range(m):
        index, num = map(int, input().split())

        index -= 1

        for j in range(1, num + 1):
            if 0 <= index - j and index + j < n:
                left = stones[index - j]
                right = stones[index + j]

                if left == right:
                    if left == 0:
                        stones[index - j] = 1
                        stones[index + j] = 1
                    elif left == 1:
                        stones[index - j] = 0
                        stones[index + j] = 0

                # print(stones)

    result = ""
    for s in stones:
        result += str(s) + " "

    print(f"#{test_case} {result}")
