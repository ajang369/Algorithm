# 정점의 부모 찾는 역할
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

# 두 정점 연결하는 역할
def union(a, b, parents):
    root_a = find(a)
    root_b = find(b)
    if root_a > root_b:
        parents[root_a] = root_b
    else:
        parents[root_b] = root_a


V, E = map(int, input().split())

# 입력받은거 트리의 정점으로 받기
tree = []
# 각 정점의 부모 - 초기 설정은 자기 자신
parents = [i for i in range(V+1)]
# 찾은 간선 수 / 총 가중치
cnt = 0
weight = 0

for i in range(E):
    a, b, cost = map(int, input().split())
    tree.append((cost, a, b))
tree.sort()

# 모든 정점 탐색
for node in tree:
    cost, a, b = node
    # 두 정점의 부모가 다르면 union해줌
    if find(a) != find(b):
        union(a, b, parents)
        # 가중치에 비용 더해주고 찾은 간선 수에 +1
        weight += cost
        cnt += 1
        # 모든 정점의 수 - 1 = 찾아야할 간선 수
        if cnt == V-1:
            break
print(weight)