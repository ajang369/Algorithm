x, y = map(int, input().split())

def gcd(a,b):
    while b:
        if a>b:
            a,b=b,a
        b = b%a
    return a

res = x*y // gcd(x,y)
print(res)