n=int(input())
li = list(map(int, input().split()))
k = int(input())
res = 0
li.sort()

x, y = 0, n-1
while x != y:
    if li[x] + li[y] < k:
        x += 1
    elif li[x]+li[y] > k:
        y -= 1
    else:
        res += 1
        x += 1
print(res)