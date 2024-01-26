n, m, k = map(int, input().split())
l = sorted(list(map(int, input().split())))
sum = 0
add = 0

for i in range(m):
    if(add < k):
        sum += l[-1]
        add += 1
    else:
        sum += l[-2]
        add = 0

print(sum)