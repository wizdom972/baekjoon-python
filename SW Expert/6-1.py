import sys
input = sys.stdin.readline

for test_case in range(1, 11):
    n = int(input())

    tree = []
    for i in range(n):
        tree.append(input().split())

    result = 1

    for node in tree:
        num, val, *children = node

        if val.isdigit():
            if children:
                result = 0

        else:
            if len(children) != 2:
                result = 0

    print(f"#{test_case} {result}")