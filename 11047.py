n, k = map(int, input().split())

a = [0] * n
for i in range(n):
    a[i] = int(input())

num = 0
for j in range(1, 1 + n):
    if a[-j] > k:
        pass
    else:
        num += k // a[-j]
        k = k % a[-j]

print(num)