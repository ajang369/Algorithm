import sys
input = sys.stdin.readline
INF = 2**32

k,n = map(int, input().split())
li = []
for _ in range(k):
    li.append(int(input()))


def Check(mid):
    cnt = 0
    for i in range(k):
        if li[i] >= mid:
            cnt += (li[i]//mid)
    return cnt >= n

low = 0
high = INF

while (low+1 < high):
    mid = (low+high)//2
    
    if Check(mid):
        low = mid
    else:
        high = mid
print(int(low))