import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
tower = list(map(int, input().split()))

received = [0] * n

stack = deque([(tower[0], 1)])

for i in range(1, n):
    curTower = tower[i]
    curIndex = i+1

    if stack[-1][0] < curTower:
        while stack and stack[-1][0] < curTower:
            stack.pop()

        if stack:
            t, idx = stack[-1]
            received[i] = idx

        stack.append((curTower, curIndex))
    else:
        t, idx = stack[-1]
        received[i] = idx

        stack.append((curTower, curIndex))

print(*list(received))