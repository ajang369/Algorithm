dx = [-1, 0, 1]
r, c = map(int, input().split())
pipe = []
for _ in range(r):
    tmp = list(input())
    pipe.append(tmp)

def dfs(x, y):
    # 끝에 도달하면 dfs종료
    if y == c-1:
        return True

    for i in range(3):
        ny = y+1
        nx = x+dx[i]
        if 0 <= ny < c and 0 <= nx < r and pipe[nx][ny] != 'x':
            pipe[nx][ny] = 'x'
            # 열 끝까지 도달했으면 리턴하고 종료
            if dfs(nx, ny):
                return True
    # 끝까지 못갔으니까 false
    return False

result = 0
for i in range(r):
    flag = dfs(i, 0)
    if flag:
        result += 1

print(result)