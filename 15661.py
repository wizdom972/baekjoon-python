from itertools import combinations

# 입력 받기
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

# 최소 차이 초기값 설정
min_diff = int(1e9)

# 팀 조합을 N//2명까지만 구하고 나머지 팀은 자동으로 결정됨

for k in range(1, n // 2 + 1):
    for start_team in combinations(range(n), n // 2):
        start_team = list(start_team)
        link_team = list(set(range(n)) - set(start_team))

        # 두 팀의 능력치 계산
        start_sum = 0
        link_sum = 0

        for i in range(n // 2):
            for j in range(i + 1, n // 2):
                start_sum += (
                    s[start_team[i]][start_team[j]] + s[start_team[j]][start_team[i]]
                )
                link_sum += (
                    s[link_team[i]][link_team[j]] + s[link_team[j]][link_team[i]]
                )

        # 능력치 차이 갱신
        diff = abs(start_sum - link_sum)
        min_diff = min(min_diff, diff)

print(min_diff)
