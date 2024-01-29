n = int(input())
score = [int(input()) for _ in range(n)]

num = 0
if n > 1:
    for i in range(2, n + 1):
        if score[-i] >= score[-(i - 1)]:
            num += (score[-i] - score[-(i - 1)] + 1)
            score[-i] = score[-(i - 1)] - 1

print(num)