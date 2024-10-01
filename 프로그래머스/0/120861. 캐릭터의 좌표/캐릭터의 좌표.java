class Solution {
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {1, -1, 0, 0};
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = {0, 0};
        
        int x = 0;
        int y = 0;
        int maxX = (board[0]-1)/2;
        int maxY = (board[1]-1)/2;
        
        for (int i = 0; i < keyinput.length; i++) {

            switch(keyinput[i]) {
                case "up":
                    x += dx[0];
                    y += dy[0];
                    break;
                case "down":
                    x += dx[1];
                    y += dy[1];
                    break;
                case "left":
                    x += dx[2];
                    y += dy[2];
                    break;
                case "right":
                    x += dx[3];
                    y += dy[3];  
                    break;
            }
            if (x > maxX)
                x = maxX;
            if (x < -maxX)
                x = -maxX;
            if (y > maxY)
                y = maxY;
            if (y < -maxY)
                y = -maxY;
            
        }
        
            
            
        answer[0] = x;
        answer[1] = y;
        return answer;
    }
}