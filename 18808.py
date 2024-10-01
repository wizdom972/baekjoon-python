# 스티커 노트북에 붙이기
def add_sticker(x, y, sticker_set):
    for loc in sticker_set:
        a, b = loc

        notebook.add((a + x, b + y))


# 시계방향으로 90도 스티커 돌리기
def rotate_90(r, c, sticker_set):
    new_sticker = set()

    for loc in sticker_set:
        x, y = loc

        new_sticker.add((y, r - x - 1))

    return (c, r, new_sticker)



# x, y 위치에서 시작하는 스티커를 붙였을 때
# 붙일 수 있는지 판단하는 함수
def check_loc(x, y, sticker_set):
    moved_sticker_loc = set()
    
    for loc in sticker_set:
        a, b = loc

        moved_sticker_loc.add((a + x, b + y))

    if notebook & moved_sticker_loc:
        return -1, -1
    
    else:
        return x, y


# 스티커를 붙일 수 있는 곳을 찾는 함수
# 붙일 곳을 찾았다면, 가장 왼쪽 위의 위치를 리턴
def find_sticker_loc(r, c, sticker_set):
    x = y = -1

    for i in range(n-r+1):
        flag = False

        for j in range(m-c+1):
            x, y = check_loc(i, j, sticker_set)

            if x != -1 and y != -1:
                flag = True
                break

        if flag:
            break

    return x, y



n, m, k = map(int, input().split())

stickers = []
for _ in range(k):
    r, c = map(int, input().split())
    
    sticker = []
    for _ in range(r):
        sticker.append(list(map(int, input().split())))


    # 스티커의 노란부분 좌표를 set에 저장해줌
    sticker_set = set()
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                sticker_set.add((i, j))

    stickers.append((r, c, sticker_set))

# print(stickers)

notebook = set()

# 모든 스티커에 대해서
for sticker in stickers:
    r, c, sticker_set = sticker

    # 90도씩 돌려가며 스티커를 붙일 위치를 탐색함
    for _ in range(4):
        x, y = find_sticker_loc(r, c, sticker_set)

        # 만약 지금 상태에서 스티커를 못 붙인다면 90도 회전
        if x == -1 and y == -1:
            r, c, sticker_set = rotate_90(r, c, sticker_set)

        # 스티커를 붙일 위치를 찾았다면 스티커 붙이기
        else:
            add_sticker(x, y, sticker_set)
            break

print(len(notebook))
