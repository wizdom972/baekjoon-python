T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    memory = list(map(int, list(input())))
    
    result = 0
    if memory[0] == 1:
        result += 1

    for i in range(len(memory) - 1):
        if memory[i] != memory[i + 1]:
            result += 1
        

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
