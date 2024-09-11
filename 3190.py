from collections import deque

n = int(input())
k = int(input())

apples = set()
for _ in range(k):
    x, y = map(int, input().split())

    apples.add((x - 1, y - 1))

l = int(input())

snake_dir = deque([])
for _ in range(l):
    t, dirc = input().split()

    t = int(t)
    snake_dir.append((t, dirc))

snake = deque([(0, 0)])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

time = 0
cur_dir = 0

while True:
    time += 1

    h_x = snake[0][0]
    h_y = snake[0][1]

    head = (h_x + dx[cur_dir], h_y + dy[cur_dir])

    if head in snake or not (0 <= head[0] < n) or not (0 <= head[1] < n):
        break

    snake.appendleft(head)

    if head in apples:
        apples.remove(head)
    else:
        snake.pop()

    if snake_dir and time == snake_dir[0][0]:
        if snake_dir[0][1] == "L":
            cur_dir -= 1
            cur_dir %= 4

        elif snake_dir[0][1] == "D":
            cur_dir += 1
            cur_dir %= 4

        snake_dir.popleft()

print(time)
