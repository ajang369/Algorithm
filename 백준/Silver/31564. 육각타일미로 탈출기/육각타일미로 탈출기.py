# 육각타일미로 탈출기
from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
miro = []
for _ in range(n):
    miro.append([0] * m)

for i in range(k):
    x,y = map(int, input().split())
    miro[x][y] = -1
# 홀수
odd_dx = [0, 0, 1, -1, 1, -1]
odd_dy = [1, -1, 0, 0, 1, 1]
# 짝수
even_dx = [0, 0, 1, -1, 1, -1]
even_dy = [1, -1, 0, 0, -1, -1]

def bfs(a, b):
    q = deque()
    q.append((a,b))
    while q:
        x, y = q.popleft()
        if x%2 == 0:
            for i in range(6):
                nx = x+even_dx[i]
                ny = y+even_dy[i]
                if 0<=nx<n and 0<=ny<m and miro[nx][ny] == 0:
                    q.append((nx, ny))
                    miro[nx][ny] = miro[x][y] + 1
        else:
            for i in range(6):
                nx = x+odd_dx[i]
                ny = y+odd_dy[i]
                if 0<=nx<n and 0<=ny<m and miro[nx][ny] == 0:
                    q.append((nx, ny))
                    miro[nx][ny] = miro[x][y] + 1
bfs(0,0)
if miro[n-1][m-1] == 0:
    print(-1)
else:
    print(miro[n-1][m-1])