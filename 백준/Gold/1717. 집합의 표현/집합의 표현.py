import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def parent_union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for i in range(m):
    num, a, b = map(int, input().split())
    if num == 0:
        parent_union(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print(' YES')
        else:
            print(' NO')

    # print('테이블: ', end=' ')
    # print(parent)