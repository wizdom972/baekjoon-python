def inorder(tree, node, s):
    num, val, *children = node

    if not children:
        s.append(val)
    else:
        inorder(tree, tree[int(children[0])], s)
        s.append(val)

        if len(children) > 1:
            inorder(tree, tree[int(children[1])], s)
    

for test_case in range(1, 11):
    n = int(input())

    tree = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        tree[i] = input().split()

    string = []

    inorder(tree, tree[1], string)

    result = "".join(string)

    print(f"#{test_case} {result}")