import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
l = list(map(int, input().split()))
l.sort()

cnt = 0
i, j = 0, n - 1

while i < j:
    if l[i] + l[j] == m:
        cnt += 1
        i += 1
        j -= 1
    elif l[i] + l[j] > m:
        j -= 1
    else:   #l[i] + l[j] < m
        i += 1

print(cnt)