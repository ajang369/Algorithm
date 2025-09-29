import sys
input = sys.stdin.readline

n=int(input())
km=list(map(int, input().split()))
liter=list(map(int, input().split()))

res = km[0]*liter[0]    # 출력값. 초기는 첫 번째 주유소에서 출발
cost=liter[0]           # 최저가를 갱신하기 위한 변수
dist=0                  # 가야하는 거리

for i in range(1, n-1):
    if cost > liter[i]:     # 새로운 최저가를 찾았을 때
        res += dist*cost    # 지금까지 누적된 거리 * 현재 최저가
        dist = km[i]        # 가야하는 거리 갱신
        cost = liter[i]     # 최저가 갱신
    else:   # 새로운 주유소가 최저가가 아닐 때
        dist += km[i]   # 거리 더해줌

    if i == n-2:    # n-2가 마지막임
        res += dist*cost
print(res)