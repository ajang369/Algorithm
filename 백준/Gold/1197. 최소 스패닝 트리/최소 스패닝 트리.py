import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

v, e = map(int, input().split())
parent = [i for i in range(v+1)]
graph = []
for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))
graph.sort()

# 부모찾기
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

# 공통 부모로 묶기
def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return
    if root_a > root_b:
        parent[root_a] = root_b
    else:
        parent[root_b] = root_a

def kruskal():
    weight = 0
    for cost, st, en in graph:
        if find(st) != find(en):
            weight += cost
            union(st, en)
    return weight

result = kruskal()
print(result)