import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int, input().split())
m = len(str(n))

visited = set()

def bfs(n):
    visited.add((n,0))
    queue = deque([[n,0]])
    result = 0
    while queue:
        num, count = queue.popleft()
        if count == k:
            result = max(num, result)
            continue
        
        temp = list(str(num))
        for i in range(m-1):
            for j in range(i+1, m):
                # 0이 맨 앞에 올 수 없는 경우
                if i == 0 and temp[j] == '0':
                    continue

                temp[i], temp[j] = temp[j], temp[i]
                change = int(''.join(temp))
                if (change, count+1) not in visited:
                    queue.append((change, count+1))
                    visited.add((change, count+1))
                temp[i], temp[j] = temp[j], temp[i]
    if result:
        return result
    else:
        return -1


print(bfs(n))