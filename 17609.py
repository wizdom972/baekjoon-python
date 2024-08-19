def check_palindrome(s, left, right, chance):
    while left < right:
        if s[left] != s[right]:
            if chance == 0:
                return 2  # 이미 기회를 소진한 경우, 더 이상 회문이 될 수 없음
            # 한 번의 기회를 사용하여 양쪽에서 하나씩 문자를 제거해본다.
            if check_palindrome(s, left + 1, right, chance - 1) == 0 or check_palindrome(s, left, right - 1, chance - 1) == 0:
                return 1  # 유사 회문
            else:
                return 2  # 회문도 유사 회문도 아님
        left += 1
        right -= 1
    return 0  # 회문

def classify_string(s):
    return check_palindrome(s, 0, len(s) - 1, 1)

T = int(input())
results = []
for _ in range(T):
    string = input().strip()
    results.append(classify_string(string))

for result in results:
    print(result)
