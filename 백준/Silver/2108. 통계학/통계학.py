import sys
input = sys.stdin.readline

n=int(input())

li = []
for _ in range(n):
    num = int(input())
    li.append(num)
li.sort()

print(round(sum(li)/n))
print(li[n//2])

diction = dict()
for i in li:
    if i in diction:
        diction[i] += 1
    else:
        diction[i] = 1
mx = max(diction.values())
mx_li = []

for i in diction:
    if diction[i] == mx:
        mx_li.append(i)
mx_li.sort()

if len(mx_li) > 1:
    print(mx_li[1])
else:
    print(mx_li[0])

print(max(li)-min(li))