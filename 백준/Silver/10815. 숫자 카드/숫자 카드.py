n=int(input())
first = list(map(int, input().split()))
m=int(input())
second = list(map(int, input().split()))

diction = {}
for i in second:
    diction[i] = 0

res=[]
for j in first:
    if j in diction:
        diction[j] = 1
print(*list(diction.values()))