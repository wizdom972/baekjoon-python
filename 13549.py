import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

INF = int(1e9)

time = [INF] * 100001
time[n] = 0

q = deque([n])

while q:
    v = q.popleft()
    
    if v == k:
        print(time[v])
        break

    if 0 <= 2*v <= 100000 and time[2*v] == INF:
        q.append(2*v)
        time[2*v] = time[v]
    
    for nv in (v-1, v+1):
        if 0 <= nv <= 100000 and time[nv] == INF:
            q.append(nv)

            t = time[nv]

            if t > time[v] + 1:
                time[nv] = time[v] + 1