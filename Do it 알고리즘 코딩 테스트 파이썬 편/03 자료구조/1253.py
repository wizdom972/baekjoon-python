import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

cnt = 0

for i in range(n):
    s, e = 0, n - 1

    while s < e:
        if a[s] + a[e] == a[i]:
            if s != i and e != i:
                cnt += 1
                break
            elif s == i:
                s += 1
            elif e == i:
                e -= 1
        elif a[s] + a[e] > a[i]:
            e -= 1
        else:   #a[s] + a[e] < a[i]
            s += 1

print(cnt)