import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(0)

else:
    visited = [0] * (n + 1)
    q = deque([1])

    while q:
        x = q.popleft()

        if x + a[x - 1] >= n:
            print(visited[x] + 1)
            break

        for i in range(1, a[x - 1] + 1):
            if visited[x + i] == 0:
                q.append(x + i)
                visited[x + i] = visited[x] + 1

    else:
        print(-1)