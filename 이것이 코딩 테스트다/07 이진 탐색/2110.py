import sys
input = sys.stdin.readline

n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]

x.sort()

start = 1
end = x[-1] - x[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    val = x[0]
    count = 1

    for i in range(n):
        if x[i] >= val + mid:
            val = x[i]
            count += 1
    
    if count < c:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)