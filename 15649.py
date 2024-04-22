import sys
input = sys.stdin.readline

def perm(arr, n):
    result = []

    if n > len(arr):
        return result
    
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])

            for p in perm(ans, n - 1):
                result.append([arr[i]] + p)
    
    return result

n, m = map(int, input().split())

arr = [*range(n+1)][1:]

for p in perm(arr, m):
    print(*p)