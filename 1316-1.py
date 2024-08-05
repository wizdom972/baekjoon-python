import sys
input = sys.stdin.readline

n = int(input())

result = n

for i in range(n):
  s = input()
  sset = list(set(s))

  for alphabet in sset:
    alphabetNum = s.count(alphabet)

    if s.find(alphabet * alphabetNum) == -1:
      result -= 1
      break
    else:
      pass

print(result)