n, k = map(int, input().split())
li = []
for i in range(1, k+1):
    tmp = n * i
    a = str(tmp)
    rev = a[::-1]
    li.append(int(rev))
print(max(li))