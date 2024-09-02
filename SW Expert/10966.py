from collections import deque


def bfs_min_distance_to_water(n, m, grid):
    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS 큐와 거리 배열 초기화
    queue = deque()
    distance = [[-1] * m for _ in range(n)]

    # 모든 물(W) 위치를 큐에 추가하고, 초기 거리를 0으로 설정
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "W":
                queue.append((i, j))
                distance[i][j] = 0

    # BFS 수행
    while queue:
        x, y = queue.popleft()

        # 인접한 칸을 검사
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

    # 모든 땅(L)에 대해 최소 이동 횟수의 합 계산
    total_distance = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "L":
                total_distance += distance[i][j]

    return total_distance


# 입력 처리 및 테스트 케이스 실행
t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]

    # 결과 출력
    result = bfs_min_distance_to_water(n, m, grid)
    print(f"#{test_case} {result}")
