from collections import deque

def solution(land):
    answer = 0
    
    n = len(land)
    m = len(land[0])
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    id = 2
    visited = [[False] * m for _ in range(n)]
    
    def bfs(sx, sy, i, visited):
        visited[sx][sy] = True
        land[sx][sy] = i
        area = 1
        
        q = deque([(sx, sy)])
        
        while q:
            x, y = q.popleft()
            
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and land[nx][ny] == 1:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        land[nx][ny] = i
                        area += 1
                        
        return area
        
    
    chunks = {}
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                chunks[id] = bfs(i, j, id, visited)
                id += 1
    
    oil = [0] * m
    
    for j in range(m):
        temp = []
        
        for i in range(n):
            if land[i][j] > 1:
                temp.append(land[i][j])
                
        stemp = list(set(temp))
        
        for t in stemp:
            oil[j] += chunks.get(t)
                                      
    answer = max(oil)
    
    return answer