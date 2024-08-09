from collections import deque


n,k = map(int, input().split())
location = [0] * (10**5 + 1)

def bfs(n):
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            print(location[x])
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i <= 10**5 and not location[i]:
                location[i] = location[x] + 1
                q.append(i)

bfs(n) 