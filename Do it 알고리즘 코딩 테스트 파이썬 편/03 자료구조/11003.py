import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
a = list(map(int, input().split()))

temp = deque()

for i in range(n):
    while temp and temp[-1][1] > a[i]:
        temp.pop()
    
    temp.append((i, a[i]))

    if i - l >= temp[0][0]: #첫번째 인덱스
        temp.popleft()

    print(temp[0][1], end=" ")