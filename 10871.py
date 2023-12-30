listNum, pivot = map(int, input().split())
list = list(map(int, input().split()))
result = []

for i in list:
    if i < pivot:
        result.append(i)

print(*result)