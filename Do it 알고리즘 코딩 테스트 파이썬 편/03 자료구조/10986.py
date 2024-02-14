import sys
from itertools import accumulate
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))

count = 0
sumList = list(accumulate(l))

for i in range(n):
    sumList[i] %= m

count += sumList.count(0)

for i in range(m):
    temp = sumList.count(i)
    count += (temp * (temp - 1) // 2)

print(count)