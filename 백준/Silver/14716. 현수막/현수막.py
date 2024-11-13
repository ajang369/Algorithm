from collections import deque

m,n = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))

dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

result = 0
def bfs(a, b):
    global result
    q = deque()
    q.append((a, b))
    graph[a][b] = 0

    while q:
        y, x = q.popleft()

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((ny, nx))


for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            result += 1
            bfs(i, j)

print(result)