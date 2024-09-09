def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a > root_b:
        parents[root_a] = root_b
    else:
        parents[root_b] = root_a

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    parents = [i for i in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        if find(a) == find(b):
            continue
        union(a, b)

    root = set()
    for i in range(1, n+1):
        root.add(find(i))
    print(f'#{test_case} {len(root)}')