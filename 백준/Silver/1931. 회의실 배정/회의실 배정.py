import sys
input = sys.stdin.readline

n = int(input())
count = 0
time = [[0]*2 for _ in range(n)]
for i in range(n):
    a,b = map(int, input().split())
    time[i][0] = a
    time[i][1] = b
time.sort(key=lambda x: (x[0]))
time.sort(key=lambda x: (x[1]))
# 시작 시간 기준으로 오름차순 하고 나서 끝나는 시간 기준으로 오름차순

last = 0
count = 0
for i, j in time:
    if i >= last:
        count += 1
        last = j
print(count)