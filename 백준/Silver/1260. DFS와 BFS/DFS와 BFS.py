import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque

n, m, r = map(int, input().split())
visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)
graph = [[] for _ in range(n+1)]
dfs_path = []
bfs_path = []

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort()

def dfs(start):
    visited_dfs[start] = 1
    dfs_path.append(start)

    for i in graph[start]:
        if visited_dfs[i] == 0:
            dfs(i)
    return

def bfs(start):
    visited_bfs[start] = 1
    need_visit = deque([start])
    while need_visit:
        node = need_visit.popleft()
        bfs_path.append(node)

        for i in graph[node]:
            
            if visited_bfs[i] == 0:
                need_visit.append(i)
                visited_bfs[i] = 1

dfs(r)
bfs(r)

print(*dfs_path)
print(*bfs_path)