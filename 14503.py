n, m = map(int, input().split())
r, c, direct = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

clean_room_num = 0
robot_x = r
robot_y = c

while True:
    # print(f"*** {robot_x} {robot_y} ***")

    if room[robot_x][robot_y] == 0:
        room[robot_x][robot_y] = -1
        clean_room_num += 1

    count = 0
    go_to_1 = False

    for i in range(4):
        nx = robot_x + dx[i]
        ny = robot_y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if room[nx][ny] == 0:  # 3
                direct = (direct - 1) % 4

                front_x = robot_x + dx[direct]
                front_y = robot_y + dy[direct]

                if (
                    0 <= front_x < n
                    and 0 <= front_y < m
                    and room[front_x][front_y] == 0
                ):
                    robot_x, robot_y = front_x, front_y
                    go_to_1 = True
                    break

            else:  # 2
                count += 1

        else:  # 2
            count += 1

    if go_to_1:
        continue

    if count == 4:  # 2
        back_x = robot_x - dx[direct]
        back_y = robot_y - dy[direct]

        if 0 <= back_x < n and 0 <= back_y < m:
            if room[back_x][back_y] != 1:
                robot_x, robot_y = back_x, back_y
                continue

            else:
                print(clean_room_num)
                break
