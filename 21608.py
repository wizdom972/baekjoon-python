dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]



def find_loc(student):
    candi = []


    for i in range(n):
        for j in range(n):
            if class_room[i][j] == 0:
                like_num = empty_num = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        if class_room[nx][ny] in like_list[student]:
                            like_num += 1

                        elif class_room[nx][ny] == 0:
                            empty_num += 1

                        candi.append((-like_num, -empty_num, i, j))

    candi.sort()

    # print(student_num)
    # print(candi)

    l, e, x, y = candi[0]

    class_room[x][y] = student

def cal_score():
    global score

    for i in range(n):
        for j in range(n):
            like_num = 0
            student = class_room[i][j]

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < n and 0 <= ny < n:
                    if class_room[nx][ny] in like_list[student]:
                        like_num += 1

            if like_num == 1:
                score += 1
            elif like_num == 2:
                score += 10
            elif like_num == 3:
                score += 100
            elif like_num == 4:
                score += 1000


n = int(input())

class_room = [[0] * n for _ in range(n)]

like_list = [[] for _ in range(n ** 2 + 1)]
for _ in range(n**2):
    student_num, *like = list(map(int, input().split()))

    like_list[student_num] = like

    find_loc(student_num)

score = 0

cal_score()

print(score)