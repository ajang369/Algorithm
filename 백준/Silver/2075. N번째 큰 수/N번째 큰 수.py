import heapq

N = int(input())

max_heap = []
for _ in range(N):
    li = list(map(int, input().split()))
    if not max_heap:
        for num in li:
            heapq.heappush(max_heap, num)
        
    else:
        for num in li:
            if max_heap[0] < num:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, num)

print(heapq.heappop(max_heap))