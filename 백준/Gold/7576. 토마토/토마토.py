from collections import deque
import sys
input = sys.stdin.readline
m,n=map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

box = []
for _ in range(n):
    box.append(list(map(int, input().split())))

def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and box[nx][ny] == 0:
                queue.append((nx,ny))
                box[nx][ny] = box[x][y] + 1

queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])

bfs()
res = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit(0)
    res = max(res, max(box[i]))
print(res-1)