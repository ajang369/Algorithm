n,k=map(int, input().split())
stu = [[0 for _ in range(7)] for _ in range(2)] 
for _ in range(n):
    s,y=map(int, input().split())
    stu[s][y] += 1
res = 0
for i in stu:
    for j in i:
        if j%k == 0:
            res += j//k
        else:
            res += (j//k + 1)
print(res)