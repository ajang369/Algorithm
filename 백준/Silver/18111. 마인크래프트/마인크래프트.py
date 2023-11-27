import sys
input = sys.stdin.readline
n,m,b=map(int, input().split())
INF = 1e9

li = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    for i in tmp:
        li.append(i)

expense = []

for high in range(257):
    minus, plus = 0, 0
    for i in li:
        tmp = high - i
        if tmp >= 0:
            plus += tmp
        else:
            minus -= tmp
    if minus + b - plus < 0:
        expense.append(INF)
    else:
        total = minus*2 + plus
        expense.append(total)
mn = min(expense)
res = []
for i in range(len(expense)):
    if expense[i] == mn:
        res.append(i)
print(mn, res[-1])