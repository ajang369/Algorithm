k=int(input())
li = []
for _ in range(k):
    n=int(input())
    if n != 0:
        li.append(n)
    else:
        if li:
            li.pop()
print(sum(li))