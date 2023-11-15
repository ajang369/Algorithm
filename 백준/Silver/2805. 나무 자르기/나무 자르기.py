n,m=map(int, input().split())
li = list(map(int, input().strip().split()))
INF = 1e9

def Check(mid):
    sum = 0
    for i in range(n):
        if li[i] > mid:
            sum += li[i] - mid
    return sum >= m

low = 0
high = INF

while (low + 1 < high):
    mid = (low+high)//2
    
    if Check(mid):
        low = mid
    else:
        high = mid

print(int(low))