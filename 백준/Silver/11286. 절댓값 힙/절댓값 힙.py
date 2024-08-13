import heapq
import sys
input = sys.stdin.readline

N = int(input())
hq = []
for i in range(N):
    a = int(input())
    if a == 0:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
    else:
        heapq.heappush(hq, (abs(a), a))