from collections import deque

k = int(input())
w, h = map(int, input().split())
graph = []
for i in range(h):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

hx = [2, 1, -2, -1, 1, 2, -2, -1]
hy = [-1, -2, 1, 2, 2, 1, -1, -2]
visited = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]
# [세로][가로][이동 수]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        x, y, z = q.popleft()
        if x == h-1 and y == w-1:
            return visited[x][y][z]-1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny][z] and graph[nx][ny] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))

        if z < k:
            for j in range(8):
                mx = x + hx[j]
                my = y + hy[j]
                if 0 <= mx < h and 0 <= my < w:
                    if graph[mx][my] == 0 and not visited[mx][my][z+1]:
                        visited[mx][my][z+1] = visited[x][y][z] + 1
                        q.append((mx, my, z+1))
    return -1

answer = bfs()
print(answer)