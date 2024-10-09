import java.util.Arrays;

class Solution
{
    public int solution(int [][]board)
    {
        int n = board.length;    // 행 row
        int m = board[0].length; // 열 column
            
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                if (board[i][j] == 1) {
                    // 1,2,3사분면의 숫자 찾기
                    int one = board[i][j-1];
                    int two = board[i-1][j-1];
                    int thr = board[i-1][j];

                    board[i][j] = Math.min(one, Math.min(two, thr)) + 1;
                }
            }
        }
        
        int MAX = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                MAX = Math.max(MAX, board[i][j]);
            }
        }
        // System.out.println(Arrays.deepToString(board));
        int answer = MAX*MAX;

        return answer;
    }
}