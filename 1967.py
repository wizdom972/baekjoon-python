import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())

    tree[p].append((c, w))
    tree[c].append((p, w))

def find_fartest_node(start):
    visited = [False] * (n+1)
    dist = [0] * (n+1)

    def dfs(node):
        visited[node] = True

        for child in tree[node]:
            c_node, weight = child

            if not visited[c_node]:
                dist[c_node] = dist[node] + weight
                dfs(c_node)

    dfs(start)
    fartest_dist = max(dist)
    fartest_node = dist.index(fartest_dist)

    return fartest_node, fartest_dist

node_a, dist_to_a = find_fartest_node(1)
node_b, dist_to_b_from_a = find_fartest_node(node_a)

print(dist_to_b_from_a)