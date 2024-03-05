import sys
input = sys.stdin.readline

n, m = map(int, input().split())
course = list(map(int, input().split()))
              
start = max(course)
end = sum(course)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    size = 0

    if mid < sum(course):
        for i in range(n):
            size += course[i]

            if size > mid:
                count += 1
                size = course[i]    

    if count > m:
        start = mid + 1
    else:
        end = mid - 1
        result = mid

print(result)