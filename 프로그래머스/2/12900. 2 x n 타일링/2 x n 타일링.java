class Solution {
    public int solution(int n) {
        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;
        // dp[3] = 3, dp[4] = 5, dp[5] = 8
        // 이런 식으로 [i-2] + [i-1]을 더하면 된다.
        for (int i = 3; i <=n; i++) {
            dp[i] = (dp[i-2] + dp[i-1])%1000000007;
        }
        
        int answer = dp[n];
        return answer;
    }
}