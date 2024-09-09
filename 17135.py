from itertools import combinations
import copy


def move_enemy():
    global temp_board

    new_board = [[] for _ in range(n)]

    new_board[0] = [0] * m

    for i in range(1, n):
        new_board[i] = temp_board[i - 1]

    temp_board = new_board


def find_enemy(archer_col, d):
    enemies = []
    archer_pos = (n, archer_col)

    for i in range(n):
        for j in range(m):
            if temp_board[i][j] == 1:
                dist = abs(i - n) + abs(j - archer_col)

                if dist <= d:
                    enemies.append((dist, i, j))

    enemies.sort(key=lambda x: (x[0], x[2]))

    if enemies:
        return enemies[0]

    return (-1, -1, -1)


def attack_enemy(archer_pos):
    global temp_count

    to_attack = []

    for a_c in archer_pos:
        to_attack.append(find_enemy(a_c, d))

    # print(to_attack)

    for enemy in to_attack:
        if enemy == (-1, -1, -1):
            continue

        dist, x, y = enemy

        if temp_board[x][y] == 0:
            continue

        temp_board[x][y] = 0
        temp_count += 1


n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

max_count = 0

for archer_index in combinations(range(m), 3):
    # print(f"****{archer_index}****")

    enemy_num = sum([sum(row) for row in board])
    temp_count = 0
    temp_board = copy.deepcopy(board)

    while enemy_num > 0:
        attack_enemy(archer_index)
        # print("**after attack**")
        # for b in temp_board:
        #     print(b)

        move_enemy()
        # print("**after move**")
        # for b in temp_board:
        #     print(b)

        enemy_num = sum([sum(row) for row in temp_board])

    max_count = max(max_count, temp_count)

print(max_count)
