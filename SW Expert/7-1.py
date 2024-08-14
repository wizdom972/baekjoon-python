import sys
input = sys.stdin.readline

def backtrack(index, curVal):
    global minVal, maxVal
    
    if index == n - 1:
        minVal = min(minVal, curVal)
        maxVal = max(maxVal, curVal)

        return

    for i in range(4):
        if operator[i]:
            calVal = calculate(curVal, nums[index + 1], i)
            operator[i] -= 1

            backtrack(index + 1, calVal)

            operator[i] += 1

def calculate(a, b, opertator_type):
    if opertator_type == 0:
        return a + b
    elif opertator_type == 1:
        return a - b
    elif opertator_type == 2:
        return a * b
    elif opertator_type == 3:
        if a < 0:
            return -(- a // b)
        return a // b

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    operator = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    minVal = int(1e9)
    maxVal = int(-1e9)

    backtrack(0, nums[0])

    print(f"#{test_case} {maxVal - minVal}")