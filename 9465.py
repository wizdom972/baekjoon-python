import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    score = [[], []]
    score[0] = list(map(int, input().split()))
    score[1] = list(map(int, input().split()))

    d = [[0] * n, [0] * n]
    d[0][0] = score[0][0]
    d[1][0] = score[1][0]

    if n >= 2:
        d[0][1] = d[1][0] + score[0][1]
        d[1][1] = d[0][0] + score[1][1]

        if n >= 3:
            for j in range(2, n):
                d[0][j] = max(d[1][j - 1], d[1][j - 2]) + score[0][j]
                d[1][j] = max(d[0][j - 1], d[0][j - 2]) + score[1][j]

    print(max(d[0][-1], d[1][-1]))    