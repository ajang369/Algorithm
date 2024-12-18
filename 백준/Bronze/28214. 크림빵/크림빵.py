n,k,p = map(int, input().split())
li = list(map(int, input().split()))

res = 0
for i in range(n):
    cnt = 0
    for j in range(k):
        if li[i*k + j] == 0:
            cnt += 1
    
    if cnt < p:
        res += 1
print(res)