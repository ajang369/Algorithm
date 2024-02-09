from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
t = int(input())
comp = [[] for _ in range(n+1)]
for _ in range(t):
    a, b = map(int, input().split())
    comp[a].append(b)
    comp[b].append(a)

visited = [False] * (n+1)
res=[]
def bfs(v):
    visited[v] = True
    q = deque([v])
    while q:
        node = q.popleft()
        res.append(node)

        for i in comp[node]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
bfs(1)
print(len(res) - 1)