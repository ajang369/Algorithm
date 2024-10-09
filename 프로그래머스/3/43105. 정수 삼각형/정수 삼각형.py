def solution(triangle):
    n = len(triangle)
    
    dp = [[0] * i for i in range(1, n+1)]
    
    dp[0][0] = triangle[0][0]
    
    for i in range(1, n):
        for j in range(len(triangle[i])-1):
            dp[i][j] = max(dp[i-1][j] + triangle[i][j], dp[i][j])
            dp[i][j+1] = max(dp[i-1][j] + triangle[i][j+1], dp[i][j+1])
    
    answer = max(dp[-1])
    
    return answer