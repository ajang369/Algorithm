import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 1

def dijk():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))      # (시작점, x, y)
    distance[0][0] = 0

    while q:
        dis, x, y = heapq.heappop(q)

        if x == n-1 and y == n-1:
            print(f'Problem {count}: {distance[x][y]}')
            break

        for i in range(4):
            next_x = x+dx[i]
            next_y = y+dy[i]

            if 0 <= next_x < n and 0 <= next_y < n:
                cost = dis + graph[next_x][next_y]

                if cost < distance[next_x][next_y]:
                    distance[next_x][next_y] = cost
                    heapq.heappush(q, (cost, next_x, next_y))


while 1:
    n = int(input())
    if n == 0:
        break
    graph = []
    distance = [[INF] * n for _ in range(n)]

    for i in range(n):
        graph.append(list(map(int, input().split())))
    
    dijk()
    count += 1