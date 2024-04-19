import sys, math
input = sys.stdin.readline

m, n = map(int, input().split())
result = []

if m <= 2 <= n:
    result.append(2)

if m % 2 == 0:
    m += 1

for i in range(max(m, 3), n+1, 2):
    isPrimary = True
    sqrt_i = int(math.sqrt(i))

    for j in range(3, sqrt_i+1, 2):
        if i % j == 0:
            isPrimary = False
            break
        
    if isPrimary:
        result.append(i)

for r in result:
    print(r)