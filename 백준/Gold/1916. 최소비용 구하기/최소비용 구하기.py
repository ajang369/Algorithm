import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

# [[출발도시, (도착도시, 비용)], ...]
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

st, en = map(int, input().split())

def dijk(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dis, now = heapq.heappop(q)

        if distance[now] < dis:
            continue

        for i in graph[now]:
            cost = dis + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijk(st)

print(distance[en])