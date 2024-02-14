import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
l = list(map(int, input().split()))

cnt = 0

for num in l:
    if l.count(m - num):
        cnt += 1

print(cnt // 2)