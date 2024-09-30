from collections import deque


dir_x = [1, -1, 0, 0]
dir_y = [0, 0, 1, -1]

r, c = map(int, input().split())
soop = []
for i in range(r):
    soop.append(list(input()))
distance = [[0] * c for _ in range(r)]

q = deque()

def bfs(dx, dy):
    while q:
        x, y = q.popleft()
        # 목적지에 고슴도치가 도달했으면 리턴
        if soop[dx][dy] == 'S':
            return distance[dx][dy]

        for i in range(4):
            nx = x + dir_x[i]
            ny = y + dir_y[i]
            if 0 <= nx < r and 0 <= ny < c:
                if soop[x][y] == 'S':
                    if soop[nx][ny] == '.' or soop[nx][ny] == 'D':
                        soop[nx][ny] = 'S'
                        distance[nx][ny] = distance[x][y] + 1
                        q.append((nx, ny))
                elif soop[x][y] == '*':
                    if soop[nx][ny] == '.' or soop[nx][ny] == 'S':
                        soop[nx][ny] = '*'
                        q.append((nx, ny))
    return "KAKTUS"


dx, dy = 0, 0
for x in range(r):
    for y in range(c):
        if soop[x][y] == 'S':
            q.append((x, y))
        elif soop[x][y] == 'D':
            dx = x
            dy = y
# 물은 나중에 추가
for x in range(r):
    for y in range(c):
        if soop[x][y] == '*':
            q.append((x, y))

result = bfs(dx, dy)
print(result)