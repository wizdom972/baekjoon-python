from itertools import combinations, permutations

n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]

team = list(combinations(range(n), int(n / 2)))
diff = 99999999999

for i in range(int(len(team) / 2)):
    teamS, teamL = team[i], team[-(i + 1)]
    start, link = 0, 0
    scoreSList = list(permutations(teamS, 2))
    scoreLList = list(permutations(teamL, 2))

    for scoreL in scoreLList:
        link += stat[scoreL[0]][scoreL[1]]
    for scoreS in scoreSList:
        start += stat[scoreS[0]][scoreS[1]]
    
    diff = min(diff, abs(start - link))

print(diff)