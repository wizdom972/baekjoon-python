import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

result = 0

def dfs(s, graph, visited, depth):
    global result

    visited[s] = True

    if depth < 5 and not graph[s]:
        return
    
    if depth == 5:
        result = 1
        return
    
    for e in graph[s]:
        if not visited[e]:
            dfs(e, graph, visited, depth+1)

            if result == 1:
                return
            
    visited[s] = False

for i in range(n):
    visited = [False] * n

    if not visited[i]:
        dfs(i, graph, visited, 1)

print(result)