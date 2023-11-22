n=int(input())
li = [0] * 10
for i in str(n):
    if i == '9' or i=='6':
        if li[9] == li[6]:
            li[9] += 1
        else:
            li[6] += 1
    else:
        li[int(i)] += 1
print(max(li))