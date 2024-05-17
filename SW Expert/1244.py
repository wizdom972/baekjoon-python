def find_max_prize(number_str, swap_count):
    max_number = 0
    length = len(number_str)
    visited = set()
    
    def swap(s, i, j):
        lst = list(s)
        lst[i], lst[j] = lst[j], lst[i]
        return ''.join(lst)
    
    def backtrack(current_number, swaps_left):
        nonlocal max_number
        
        if swaps_left == 0:
            max_number = max(max_number, int(current_number))
            return
        
        if (current_number, swaps_left) in visited:
            return
        visited.add((current_number, swaps_left))
        
        for i in range(length):
            for j in range(i + 1, length):
                swapped = swap(current_number, i, j)
                backtrack(swapped, swaps_left - 1)
    
    backtrack(number_str, swap_count)
    return max_number

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    number_str, swap_count = input().split()
    swap_count = int(swap_count)

    result = find_max_prize(number_str, swap_count)

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
