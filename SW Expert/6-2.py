from collections import deque

def postorder(tree, node, stack):
    num, val, *child = node

    if not child:
        stack.append(val)
    else:
        postorder(tree, tree[int(child[0])], stack)
        postorder(tree, tree[int(child[1])], stack)
        stack.append(val)

for test_case in range(1, 11):
    n = int(input())

    tree = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        tree[i] = input().split()

    stack = deque([])

    postorder(tree, tree[1], stack)

    s = deque([])

    for data in stack:
        if data.isnumeric():
            s.append(data)
        elif data == "+":
            two = float(s.pop())
            one = float(s.pop())

            s.append(str(one + two))
        elif data == "-":
            two = float(s.pop())
            one = float(s.pop())

            s.append(str(one - two))
        elif data == "*":
            two = float(s.pop())
            one = float(s.pop())

            s.append(str(one * two))
        elif data == "/":
            two = float(s.pop())
            one = float(s.pop())

            s.append(str(one / two))

    print(f"#{test_case} {int(float(s[0]))}")

