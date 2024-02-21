import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

d = [-1] * (n + 1)
d[x] = 0

queue = deque([x])
    
while queue:
    v = queue.popleft()

    for i in graph[v]:
        if d[i] == -1:
            d[i] = d[v] + 1
            queue.append(i)

if k in d:
    for index, val in enumerate(d):
        if val == k:
            print(index)
else:
    print(-1)