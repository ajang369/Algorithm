T = 10
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
res = -1

def dfs(x, y, miro):
    miro[x][y] = -1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 16 and 0 <= ny < 16:
            if miro[nx][ny] == 0:
                if dfs(nx, ny, miro) == 1:
                    return 1
            elif miro[nx][ny] == 3:
                return 1
    return 0


for test_case in range(1, T+1):
    t = int(input())
    miro = []
    for _ in range(16):
        miro.append(list(map(int, input())))

    x = 0
    y = 0
    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                x = i
                y = j
                break
    res = dfs(x, y, miro)
    print("#{} {}".format(t, res))