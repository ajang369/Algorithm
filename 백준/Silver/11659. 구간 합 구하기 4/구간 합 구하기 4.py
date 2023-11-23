import sys
input = sys.stdin.readline
n,m=map(int, input().split())
num = list(map(int, input().split()))
sum = [0] * (n+1)
for i in range(n):
    sum[i+1] = sum[i] + num[i]
for _ in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    res = sum[j+1] - sum[i]
    print(res)