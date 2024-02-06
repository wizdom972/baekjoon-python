n, m = map(int, input().split())
list = [0] + list(map(int, input().split()))
sumList = [0] * (n + 1)
sum = 0

for i in range(1, n + 1):
    sum += list[i]
    sumList[i] = sum

for _ in range(m):
    i, j = map(int, input().split())
    print(sumList[j] - sumList[i - 1])