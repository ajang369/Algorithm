n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):          # 거쳐가는 점
    for i in range(n):      # 시작점
        for j in range(n):  # 종료점
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for i in graph:
    print(*i)