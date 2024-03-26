import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if data[i - 1] < data[i]:
        index = i - 1

        for j in range(n-1, 0, -1):
            if data[j] > data[i - 1]:
                data[i - 1], data[j] = data[j], data[i - 1]
                result = data[:i] + list(sorted(data[i:]))

                print(*result)
                sys.exit()

print(-1)