a,b = map(int,input().split())
if a > b:
    a, b = b, a

ans = 0

if (b-a+1)%2 != 0:
    ans = (a+b)*((b-a+1)//2) + (a+b)//2
else:
    ans = (a+b)*((b-a+1)//2)
print(ans)