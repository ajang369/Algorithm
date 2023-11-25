import sys
input = sys.stdin.readline
N = int(input())
li = []
for _ in range(N):
    li.append(list(map(int, input().split())))
w, b = 0, 0

def cut(x, y, n):
    color = li[x][y]
    global w, b

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != li[i][j]:
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        w += 1
    else:
        b += 1

cut(0,0,N)
print(w)
print(b)