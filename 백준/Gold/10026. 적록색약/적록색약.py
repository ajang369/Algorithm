from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
paint = []
for _ in range(n):
    paint.append(list(input()))
visit1 = [[False] * n for _ in range(n)]
visit2 = [[False] * n for _ in range(n)]
paint_rg = [['']*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        paint_rg[i][j] = paint[i][j]
        if paint[i][j] == 'G':
            paint_rg[i][j] = 'R'

def bfs(a, b, graph, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    color = graph[a][b]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False and graph[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny))


res1, res2 = 0, 0
for i in range(n):
    for j in range(n):
        if not visit1[i][j]:
            bfs(i, j, paint, visit1)
            res1 += 1

for i in range(n):
    for j in range(n):
        if not visit2[i][j]:
            bfs(i, j, paint_rg, visit2)
            res2 += 1

print(res1, res2)