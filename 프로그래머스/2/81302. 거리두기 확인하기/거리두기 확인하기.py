from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b, place):
    q = deque()
    q.append((a, b))

    visited = [[False] * 5 for _ in range(5)]
    visited[a][b] = True  # 방문처리

    distance = [[0] * 5 for _ in range(5)]  # 거리

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 4방향 탐색
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == False:
                if place[ny][nx] == "O":
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    # 갈 수 있는 곳에는 거리 + 1
                    distance[ny][nx] = distance[y][x] + 1

                # 사람이 있는 곳일 때
                if place[ny][nx] == "P":
                    # 거리가 2이하인 경우 불가능
                    if distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        flag = 1

        # 'P'인 좌표 넣는 리스트
        people = []

        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))
        # P인 좌표에서 출발해서 bfs탐색
        for p in people:
            res = bfs(p[0], p[1], place)
            if res == 0:
                flag = 0
                break
            
        answer.append(flag)

    return answer