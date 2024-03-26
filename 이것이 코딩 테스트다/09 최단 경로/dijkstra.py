import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())

distance = [INF] * (v + 1)
graph = [[] for _ in range(v + 1)]

for i in range(e):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, vertex = heapq.heappop(q)

        if distance[vertex] < dist:
            continue
        

        for v in graph[vertex]:
            cost = dist + v[1]

            if cost < distance[v[0]]:
                distance[v[0]] = cost
                heapq.heappush(q, (cost, v[0]))

