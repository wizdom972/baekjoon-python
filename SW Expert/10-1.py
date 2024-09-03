def backtrack(board, depth):
    global max_num

    state = (depth, tuple(board))
    if state in data:
        return

    data.add(state)

    if depth == num:
        temp_num = int("".join(map(str, board)))

        if temp_num > max_num:
            max_num = temp_num

        return

    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            board[i], board[j] = board[j], board[i]
            backtrack(board, depth + 1)
            board[i], board[j] = board[j], board[i]


T = int(input())
for test_case in range(1, T + 1):
    board, num = input().split()

    board = list(map(int, (list(board))))
    num = int(num)

    max_num = 0
    data = set()

    backtrack(board, 0)

    print(f"#{test_case} {max_num}")
