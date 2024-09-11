N, M = map(int, input().split())
miro = []
dp = [[0] * (M+1) for _ in range(N+1)]
for i in range(N):
    tmp = list(map(int, input().split()))
    miro.append(tmp)

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + miro[i-1][j-1]
print(dp[-1][-1])