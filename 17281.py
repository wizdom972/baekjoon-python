import sys
input = sys.stdin.readline

inningNum = int(input())

iResult = [[] for _ in range(inningNum)]
for i in range(inningNum):
    iResult[i] = list(map(int, input().split()))

def perm(arr, n):
    result = []

    if n > len(arr):
        return result
    
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])

            for p in perm(ans, n-1):
                result.append([arr[i]] + p)

    return result

runners = list(range(1, 9))
runnersPerm = perm(runners, 8)

maxScore = 0

for runnerList in runnersPerm:
    score = 0
    runnerList = list(runnerList)
    tempRunnerList = runnerList[:3] + [0] + runnerList[3:]
    idx = 0

    for iNum in range(inningNum):
        out = 0
        bases = [False] * 3

        while out != 3:
            hit = iResult[iNum][tempRunnerList[idx]]
            idx += 1
            idx %= 9

            if hit == 1:
                score += bases[2]
                bases = [True] + bases[:2]
            elif hit == 2:
                score += (bases[2] + bases[1])
                bases = [False, True] + [bases[0]]
            elif hit == 3:
                score += (bases[2] + bases[1] + bases[0])
                bases = [False, False, True]
            elif hit == 4:
                score += ((bases[2] + bases[1] + bases[0]) + 1)
                bases = [False] * 3
            elif hit == 0:
                out += 1

    maxScore = max(maxScore, score)

print(maxScore)