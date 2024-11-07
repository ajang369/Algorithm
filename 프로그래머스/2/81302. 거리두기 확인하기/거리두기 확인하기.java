import java.util.*;

public class Solution {
    // 방향 벡터
    private static final int[] dx = {-1, 1, 0, 0};
    private static final int[] dy = {0, 0, -1, 1};

    public int[] solution(String[][] places) {
        int[] answer = new int[places.length];

        for (int i = 0; i < places.length; i++) {
            answer[i] = checkPlace(places[i]);
        }

        return answer;
    }

    private int checkPlace(String[] place) {
        // P인 좌표를 저장하는 리스트
        List<int[]> people = new ArrayList<>();

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (place[i].charAt(j) == 'P') {
                    people.add(new int[]{i, j});
                }
            }
        }

        // 각 'P' 위치마다 거리두기 검사
        for (int[] p : people) {
            int res = bfs(p[0], p[1], place);
            
            if (res == 0){
                return 0;
            }
        }

        return 1;
    }

    private int bfs(int a, int b, String[] place) {
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{a, b});

        // 방문처리
        boolean[][] visited = new boolean[5][5];
        visited[a][b] = true;

        // 거리 기록
        int[][] distance = new int[5][5];

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int y = current[0];
            int x = current[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                // 4방향 탐색
                if (nx >= 0 && nx < 5 && ny >= 0 && ny < 5 && !visited[ny][nx]) {
                    if (place[ny].charAt(nx) == 'O') {
                        queue.offer(new int[]{ny, nx});
                        visited[ny][nx] = true;
                        // 갈 수 있는 곳 거리 +1
                        distance[ny][nx] = distance[y][x] + 1;
                    }

                    // 사람이 있는 곳일 때 거리 확인
                    if (place[ny].charAt(nx) == 'P') {
                        // 거리가 2이하인 경우 불가능
                        if (distance[y][x] <= 1) {
                            return 0;
                        }
                    }
                }
            }
        }
        return 1;
    }
}
