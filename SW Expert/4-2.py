from collections import deque

priority = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2
}

for test_case in range(1, 11):
    n = int(input())
    string = input()

    stack = deque([])
    equation = deque([])

    for s in string:
        if s.isalnum():
            equation.append(s)

        elif s == "(":
            stack.append(s)

        elif s == ")":
            while stack and equation[-1] != "(":
                equation.append(stack.pop())
            equation.pop()

        else:
            while (stack and stack[-1] != "(") and priority[stack[-1]] >= priority[s]:
                equation.append(stack.pop())
            stack.append(s)

        # print(stack, equation)

    for s in equation:
        if s.isnumeric():
            stack.append(s)

        elif s == "+":
            two = stack.pop()
            one = stack.pop()

            stack.append(int(one) + int(two))

        elif s == "-":
            two = stack.pop()
            one = stack.pop()

            stack.append(int(one) - int(two))

        elif s == "*":
            two = stack.pop()
            one = stack.pop()

            stack.append(int(one) * int(two))

        elif s == "/":
            two = stack.pop()
            one = stack.pop()

            stack.append(int(one) / int(two))

    print(f"#{test_case} {int(stack.pop())}")