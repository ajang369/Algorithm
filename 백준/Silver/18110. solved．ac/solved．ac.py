import sys
input = sys.stdin.readline

n=int(input())

def _round(num):
    return int(num) + (1 if num-int(num) >= 0.5 else 0)

if n == 0:
    print(0)
else:
    li = [int(input()) for _ in range(n)]
    minus = _round(n*0.15)
    li.sort()
    total = sum(li[minus:n-minus])
    avg = total/(n-2*minus)
    print(_round(avg))