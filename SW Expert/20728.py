T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, k = map(int, input().split())
    candies = list(map(int, input().split()))

    candies.sort(reverse=True)

    result = int(1e9)
    for i in range(n-k+1):
        diff = candies[i] - candies[k+i-1]
        result = min(result, diff)

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
