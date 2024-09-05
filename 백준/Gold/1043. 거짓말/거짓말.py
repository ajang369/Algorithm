import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
truth = list(map(int, input().split()))
for i in truth[1:]:
    parent[i] = 0

party = []
for i in range(m):
    tmp = list(map(int, input().split()))
    party.append(tmp[1:])
    if tmp[0] > 1:
        for j in range(1, tmp[0]):
            union(tmp[j], tmp[j+1])

res = m
for i in party:
    for j in i:
        if find(parent[j]) == 0:
            res -= 1
            break
print(res)