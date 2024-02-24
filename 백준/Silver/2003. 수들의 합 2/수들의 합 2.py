n,m=map(int, input().split())
li = list(map(int, input().split()))
right = 1
left = 0
res = 0

while left <= right and right<=n:
    sum_li = sum(li[left:right])
    
    if sum_li == m:
        res += 1
        right += 1

    elif sum_li < m:
        right += 1
    
    else:
        left += 1
print(res)