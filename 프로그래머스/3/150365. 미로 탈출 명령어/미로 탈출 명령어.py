import sys
sys.setrecursionlimit(10**6)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
dd = ['d', 'l', 'r', 'u']
word = ''
answer = 'impossible'
flag = False

# dfs 백트래킹
def dfs(count, cur_x, cur_y, r, c, k, n, m):
    global word, answer, flag
    if flag:
        return
    
    # 현재 위치부터 목적지까지 거리
    distance = abs(cur_x - r) + abs(cur_y - c)
    
    # 현재 위치부터 목적지까지 거리보다 남은 이동 횟수가 작으면 안됨
    if k-count < distance:
        return
    # 목적지까지 거리 + (남은 횟수)가 홀수이면 불가능
    if (distance + (k-count))%2 != 0:
        return
    
    # 목적지 도착
    if count == k and cur_x == r and cur_y == c:
        answer = word
        flag = True
        return
    
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if 1 <= nx <= n and 1 <= ny <= m:
            # 백트래킹
            word += dd[i]
            dfs(count+1, nx, ny, r, c, k, n, m)
            word = word[:-1]
            

def solution(n, m, x, y, r, c, k):
    global answer, flag
    flag = False
    answer = 'impossible'

    dfs(0, x, y, r, c, k, n, m)


    return answer