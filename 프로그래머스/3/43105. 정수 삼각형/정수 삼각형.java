import java.util.Arrays;

class Solution {
    public int solution(int[][] triangle) {
        int n = triangle.length;
        int[][] dp = new int[n][];
        for (int i = 0; i < n; i++) {
            dp[i] = new int[i+1];
        }
        
        dp[0][0] = triangle[0][0];
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < triangle[i].length - 1; j++) {
                int tmp1 = triangle[i][j] + dp[i-1][j];
                dp[i][j] = Math.max(dp[i][j], tmp1);
                
                int tmp2 = triangle[i][j+1] + dp[i-1][j];
                dp[i][j+1] = Math.max(dp[i][j+1], tmp2);

            }
        }
        
        int answer = Arrays.stream(dp[n-1]).max().getAsInt();
        
        return answer;
    }
}