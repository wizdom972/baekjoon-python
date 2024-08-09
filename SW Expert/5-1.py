from collections import deque

for test_case in range(1, 11):
    n = int(input())
    numList = list(map(int, input().split()))

    q = deque(numList)
    minusNum = 1

    while True:
        front = q.popleft()
        front -= minusNum
        minusNum += 1

        if minusNum == 6:
            minusNum = 1

        if front <= 0:
            front = 0
            q.append(front)
            break

        q.append(front)

    result = " ".join(map(str, q))
    print(f"#{test_case} {result}")
