n, m, x, y, k = map(int, input().split())

map_gird = []
for _ in range(n):
    map_gird.append(list(map(int, input().split())))

command = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

dice = [0] * 6

def roll_dice(direc):
    if direc == 1:
        temp = dice[0]
        
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[2]
        dice[2] = temp

    elif direc == 2:
        temp = dice[0]

        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[3]
        dice[3] = temp

    elif direc == 3:
        temp = dice[0]

        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[1]
        dice[1] = temp
    
    elif direc == 4:
        temp = dice[0]

        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[4]
        dice[4] = temp

for i in range(k):
    direc = command[i]

    nx = x + dx[direc]
    ny = y + dy[direc]

    if 0 <= nx < n and 0 <= ny < m:
        x = nx
        y = ny

        roll_dice(direc)

        if map_gird[x][y] == 0:
            map_gird[x][y] = dice[5]
        
        else:
            dice[5] = map_gird[x][y]
            map_gird[x][y] = 0

        print(dice[0])