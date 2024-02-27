import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

for i in range(k):
    if A[i] < B[-i - 1]:
        A[i], B[-i - 1] = B[-i - 1], A[i]
    else:
        break

print(sum(A))