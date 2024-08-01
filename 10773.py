import sys
input = sys.stdin.readline

from collections import deque

k = int(input())

stack = deque([])

for i in range(k):
    num = int(input())

    if num == 0:
        stack.pop()
    else:
        stack.append(num)


print(sum(stack))