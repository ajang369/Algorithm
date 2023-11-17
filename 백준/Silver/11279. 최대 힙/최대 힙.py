import sys
import heapq
input = sys.stdin.readline

x = int(input())
li = []
for i in range(x):
    num = int(input())
    if num != 0:
        heapq.heappush(li, -num)
    else:
        if not li:
            print(0)
        else:
            print(heapq.heappop(li)*-1)