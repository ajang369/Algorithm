import math
t=int(input())
for _ in range(t):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    dist = ((x1-x2)**2+(y1-y2)**2)**0.5

    if dist == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r1+r2 == dist or abs(r2-r1) == dist:
            print(1)
        elif abs(r2-r1) < dist and dist<r1+r2:
            print(2)
        else:
            print(0)