import sys
input = sys.stdin.readline

n = int(input())

score = []
for _ in range(n):
    student = input().split()
    score.append((student[0], int(student[1]), int(student[2]), int(student[3])))

score.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))

for s in score:
    print(s[0])