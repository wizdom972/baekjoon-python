import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)

def cut(pivot, i):
    if pivot < i:
        return i - pivot
    else:
        return 0

while start <= end:
    mid = (start + end) // 2

    length = 0
    for d in data:
        length += cut(mid, d)

    if length == m:
        print(mid)
        break
    elif length > m:
        start = mid + 1
    else:   #length < m
        end = mid - 1