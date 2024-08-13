import sys, math
input = sys.stdin.readline

n, p, q = map(int, input().split())

dic = {}

def func(i):
    if i == 0:
        return 1
    
    if i in dic:
        return dic[i]
    else:
        dic[i] = func(math.floor(i / p)) + func(math.floor(i / q))
        return dic[i]

print(func(n))