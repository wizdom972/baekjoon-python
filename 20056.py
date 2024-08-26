n, m, k = map(int, input().split())

matrix = [[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    r, c, m, s, d = map(int, input().split())
    matrix[r-1][c-1].append((m, s, d))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def isAllOddOrEven(arr):
    pivot = arr[0] % 2

    for item in arr:
        if item % 2 != pivot:
            return [1, 3, 5, 7]
        
    return [0, 2, 4, 6]

def move_fire_ball():
    global matrix
    new_matrix = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                for f_ball in matrix[i][j]:
                    m, s, d = f_ball

                    nx = (i + dx[d] * s) % n
                    ny = (j + dy[d] * s) % n

                    if 0 <= nx < n and 0 <= ny < n:
                        new_matrix[nx][ny].append((m, s, d))
    
    matrix = new_matrix

def divde_fire_ball():
    global matrix
    new_matrix = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                if len(matrix[i][j]) == 1:
                    new_matrix[i][j] = matrix[i][j][:]
                elif len(matrix[i][j]) >= 2:
                    m_sum = 0
                    s_sum = 0
                    dirs = []

                    for f_ball in matrix[i][j]:
                        m_sum += f_ball[0]
                        s_sum += f_ball[1]
                        dirs.append(f_ball[2])

                    m_sum = m_sum // 5
                    s_sum = s_sum // len(matrix[i][j])
                    dirs = isAllOddOrEven(dirs)

                    if m_sum != 0 and s_sum != 0:
                        for d in dirs:
                            new_matrix[i][j].append((m_sum, s_sum, d))

    matrix = new_matrix

for _ in range(k):
    move_fire_ball()
    divde_fire_ball()

result = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            for f_ball in matrix[i][j]:
                result += f_ball[0]

print(result)