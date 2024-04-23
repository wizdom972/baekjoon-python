import sys
input = sys.stdin.readline

def perm(arr, n):
    result = []

    if n > len(arr):
        return result
    
    for i in range(len(arr)):
        if n == 1:
            for j in arr[i:]:
                result.append([j])
            break
        elif n > 1:
            ans = [j for j in arr[i:]]
            ans.remove(arr[i])

            for p in perm(ans, n-1):
                result.append([arr[i]] + p)

    return result

n, m = map(int, input().split())

arr = [*range(1, n+1)]

for p in perm(arr, m):
    print(*p)