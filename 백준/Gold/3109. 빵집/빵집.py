dx = [-1, 0, 1]
r, c = map(int, input().split())
pipe = []
for _ in range(r):
    tmp = list(input())
    pipe.append(tmp)

def dfs(x, y):
    if y == c-1:
        return True

    for i in range(3):
        ny = y+1
        nx = x+dx[i]
        if 0 <= ny < c and 0 <= nx < r and pipe[nx][ny] != 'x':
            pipe[nx][ny] = 'x'
            if dfs(nx, ny):
                return True
    return False

result = 0
for i in range(r):
    flag = dfs(i, 0)
    if flag:
        result += 1

print(result)