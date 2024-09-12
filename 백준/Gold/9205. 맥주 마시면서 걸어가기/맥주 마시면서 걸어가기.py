from collections import deque


def get_distance(start, end):
    dist = abs(start[0] - end[0]) + abs(start[1] - end[1])
    return dist

def bfs(a, b):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        distance = get_distance((x, y), festival)

        if distance <= 1000:
            print("happy")
            return

        for i in range(N):
            if not visited[i]:
                if get_distance((x, y), shop[i]) <= 1000:
                    nx = shop[i][0]
                    ny = shop[i][1]
                    visited[i] = True
                    q.append((nx, ny))
    print("sad")
    return


T = int(input())
for _ in range(T):

    N = int(input())
    home = list(map(int, input().split()))
    shop = []
    for i in range(N):
        shop.append(list(map(int, input().split())))
    festival = list(map(int, input().split()))
    visited = [False] * N

    bfs(home[0], home[1])