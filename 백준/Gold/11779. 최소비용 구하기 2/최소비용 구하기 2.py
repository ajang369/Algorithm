import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
count = [0] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    #[시작][출발, 비용]
st, en = map(int, input().split())

def dijk(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dis, now = heapq.heappop(q)
        if distance[now] < dis:
            continue

        for node, weight in graph[now]:
            cost = dis + weight

            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))
                count[node] = now

dijk(st)
print(distance[en])



path = [en]
temp = en
while temp != st:
    temp = count[temp]
    path.append(temp)

path.reverse()

print(len(path))
print(' '.join(map(str, path)))