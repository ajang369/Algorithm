import sys
input = sys.stdin.readline
A=[]
B=[]
N, M = map(int, input().split())
for n in range(N):
    A.append(list(map(int, input().split())))
M, K = map(int, input().split())
for m in range(M):
    B.append(list(map(int, input().split())))

res = [[0 for _ in range(K)] for _ in range(N)]
for n in range(N):
    for k in range(K):
        for m in range(M):
            res[n][k] += A[n][m] * B[m][k]

for i in res:
    print(*i)