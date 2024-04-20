import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())

MAX = 100000
time = [0] * (MAX + 1)

q = deque([n])

while q:
    v = q.popleft()

    if v == k:
        print(time[v])
        break

    for nv in (v-1, v+1, 2*v):
        if 0 <= nv <= MAX and not time[nv]:
            time[nv] = time[v] + 1
            q.append(nv)    