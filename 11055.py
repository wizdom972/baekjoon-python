import sys
input = sys.stdin.readline

n = int(input())
numList = list(map(int, input().split()))

dp = numList[:]

for i in range(n):
  for j in range(i):
    if numList[j] < numList[i]:
      dp[i] = max(dp[i], numList[i] + dp[j])

print(max(dp))