def backtrack(temp_lcd, index, inject_num):
    global min_inject_num

    # 더 이상 약품 투입이 불필요한 경우
    if inject_num >= min_inject_num:
        return

    # 성능검사를 통과한 경우
    if check_quality(temp_lcd):
        min_inject_num = min(inject_num, min_inject_num)
        return

    # 마지막 행까지 도달한 경우
    if index == d:
        return

    # 약품을 사용하지 않고 넘어가는 경우
    backtrack(temp_lcd, index + 1, inject_num)

    # 약품 A를 투입하는 경우
    original_row = temp_lcd[index][:]
    temp_lcd[index] = [0] * w
    backtrack(temp_lcd, index + 1, inject_num + 1)
    temp_lcd[index] = original_row  # 원래대로 복구

    # 약품 B를 투입하는 경우
    temp_lcd[index] = [1] * w
    backtrack(temp_lcd, index + 1, inject_num + 1)
    temp_lcd[index] = original_row  # 원래대로 복구


def check_quality(temp_lcd):
    for j in range(w):
        for i in range(d - k + 1):
            temp = set(temp_lcd[i + col][j] for col in range(k))
            if len(temp) == 1:  # 세로로 k개 연속된 셀의 특성이 동일한지 확인
                break
        else:
            return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    d, w, k = map(int, input().split())
    lcd = [list(map(int, input().split())) for _ in range(d)]

    # 최소 투입 횟수 초기화
    min_inject_num = int(1e12)

    # 백트래킹 시작
    backtrack(lcd, 0, 0)

    # 결과 출력
    print(f"#{test_case} {min_inject_num}")
