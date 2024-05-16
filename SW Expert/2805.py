T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())

    farm = [list(map(int, list(input()))) for _ in range(n)]

    result = 0

    for i in range(n//2+1):
        for j in range(n):
            if n//2-i <= j <= n//2+i:
                result += farm[i][j]

    for i in range(n//2+1, n):
        for j in range(n):
            if n//2-n+i+1 <= j <= n//2+n-i-1:
                result += farm[i][j]

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
