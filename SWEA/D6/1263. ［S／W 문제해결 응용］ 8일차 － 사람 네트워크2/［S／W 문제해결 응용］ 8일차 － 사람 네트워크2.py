
import heapq


def dijk(distance, start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for next in adj_list[now]:
            cost = dist + 1
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))

T = int(input())
for tc in range(1, T+1):
    graph = []
    arr = list(map(int, input().split()))
    N = arr[0]

    for i in range(N):
        st = 1+(N*i)
        en = N*(i+1)
        tmp = arr[st:en+1]
        graph.append(tmp)

    adj_list = [[] for _ in range(N)]
    for i in range(N):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                adj_list[i].append(j)

    INF = int(1e9)
    res = []
    for i in range(N):
        distance = [INF] * N
        dijk(distance, i)
        res.append(sum(distance))
    print(f'#{tc} {min(res)}')