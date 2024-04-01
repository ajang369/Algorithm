li = []
sq = [[0]*101 for _ in range(101)]
res = 0
for i in range(4):
    x1,y1,x2,y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            if sq[j][k] == 0:
                sq[j][k] += 1
                res += 1
print(res)