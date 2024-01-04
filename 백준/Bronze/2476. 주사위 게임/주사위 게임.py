n=int(input())
res=[]
for _ in range(n):
    li = [0] * 7
    nums = list(map(int, input().split()))
    for i in nums:
        li[i] += 1
    if max(li) == 1:
        res.append(max(nums)*100)
    elif max(li) == 2:
        tmp = li.index(2)
        res.append(tmp*100 + 1000)
    elif max(li) == 3:
        tmp = li.index(3)
        res.append(tmp*1000 + 10000)
print(max(res))