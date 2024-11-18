N = int(input())
INF = int(1e9)

graph = [[INF]*(N+1) for _ in range(N+1)]

while 1:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break

    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N+1):
    graph[k][k] = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = []
for i in range(1, N+1):
    max_score = 0
    for j in range(1, N+1):
        max_score = max(max_score, graph[i][j])
    answer.append(max_score)

_min = min(answer)
cnt = answer.count(_min)

idx = []
for i in range(N):
    if _min == answer[i]:
        idx.append(i+1)

print(_min, cnt)
print(*idx)