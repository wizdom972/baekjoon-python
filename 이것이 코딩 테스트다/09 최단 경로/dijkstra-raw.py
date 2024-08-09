import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))

def get_smallest_node():
    minVal = INF
    index = 0

    for i in range(1, n+1):
        if distance[i] < minVal and not visited[i]:
            index = i
    
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for (b, c) in graph[start]:
        distance[b] = c
    
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for (b, c) in graph[now]:
            cost = distance[now] + c

            if cost < distance[b]:
                distance[b] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")

    else:
        print(distance[i])