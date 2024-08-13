import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int, input().split())
friend = [[] for _ in range(n)]
visit = [False]*(n+1)
ans = False

for i in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

def dfs(s, cnt):
    global ans
    visit[s] = True

    if cnt == 4:
        ans = True
        return

    for i in friend[s]:
        if visit[i] == False:
            dfs(i, cnt+1)
    # 다음 탐색에서 다시 방문해야하므로 방문 표시 초기화
    visit[s]= False

for i in range(n):
    dfs(i, 0)
    if ans == True:
        break

if ans:
    print(1)
else:
    print(0)