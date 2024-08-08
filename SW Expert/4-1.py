from collections import deque

for test_case in range(10):
    n, s = input().split()
    n = int(n)

    stack = deque([])

    for i in range(n):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    result = "".join(stack)

    print(f"#{test_case+1} {result}")