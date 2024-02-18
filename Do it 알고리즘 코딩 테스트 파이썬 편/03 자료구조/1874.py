import sys
input = sys.stdin.readline

n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
result = []
num = 1
isFail = False

for i in range(n):
    if sequence[i] >= num:
        while sequence[i] >= num:
            stack.append(num)
            num += 1
            result.append('+')
        stack.pop()
        result.append('-')
    else: #sequence[i] < i
        n = stack.pop()
        if n > sequence[i]:
            print("NO")
            isFail = True
            break
        else:
            result.append('-')

if isFail is not True:
    for r in result:
        print(r)