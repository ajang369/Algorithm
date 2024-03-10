m = int(input())
res = 0
if m <= 30:
    res = m*0.5
else:
    m -= 30
    res = 15 + m*1.5
print(round(res, 1))