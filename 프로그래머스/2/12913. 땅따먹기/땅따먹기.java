import java.util.Arrays;

class Solution {
    int solution(int[][] land) {
        int n = land.length;
        
        int[][] dp = new int[n][4];
        for (int i = 0; i < 4; i++) {
            dp[0][i] = land[0][i];
        }
        
        for (int i = 1; i < n; i++) {
            // j = 현재 줄
            for (int j = 0; j < 4; j++) {
                // k = 이전 줄에서 같은 열이 아닌 것
                for (int k = 0; k < 4; k++) {
                    if (j == k) continue;
                    dp[i][j] = Math.max(land[i][j] + dp[i-1][k], dp[i][j]);
                }
            }
        }
        //System.out.println(Arrays.deepToString(dp));
        
        int answer = Arrays.stream(dp[n-1]).max().getAsInt();
        

        return answer;
    }
}