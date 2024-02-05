from collections import deque

n, k, m = map(int, input().split())
count = 0
ring = deque(range(1,n+1))

while ring:
    if (count // m) % 2 == 0:
        for _ in range(k - 1):
            ring.append(ring.popleft())
    else:
        for _ in range(k):
            ring.appendleft(ring.pop())
    
    count += 1
    print(ring.popleft())