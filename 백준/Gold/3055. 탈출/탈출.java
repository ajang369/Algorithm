import java.io.*;
import java.util.*;

public class Main {
    static int[] dirX = {1, -1, 0, 0};
    static int[] dirY = {0, 0, 1, -1};
    static int r, c;
    static char[][] soop;
    static int[][] distance;
    static Deque<int[]> q = new ArrayDeque<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        soop = new char[r][c];
        distance = new int[r][c];

        for (int i = 0; i < r; i++) {
            soop[i] = br.readLine().toCharArray();
        }

        int dx = 0, dy = 0;

        // 고슴도치와 목적지 좌표 탐색
        for (int x = 0; x < r; x++) {
            for (int y = 0; y < c; y++) {
                if (soop[x][y] == 'S') {
                    q.offer(new int[]{x, y});
                } else if (soop[x][y] == 'D') {
                    dx = x;
                    dy = y;
                }
            }
        }

        // 물 좌표를 큐에 추가
        for (int x = 0; x < r; x++) {
            for (int y = 0; y < c; y++) {
                if (soop[x][y] == '*') {
                    q.offer(new int[]{x, y});
                }
            }
        }

        // BFS 탐색 시작
        String result = bfs(dx, dy);
        System.out.println(result);
    }

    static String bfs(int dx, int dy) {
        while (!q.isEmpty()) {
            int[] current = q.poll();
            int x = current[0];
            int y = current[1];

            // 고슴도치가 목적지에 도착했으면 종료
            if (soop[dx][dy] == 'S') {
                return String.valueOf(distance[dx][dy]);
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dirX[i];
                int ny = y + dirY[i];

                if (nx >= 0 && nx < r && ny >= 0 && ny < c) {
                    if (soop[x][y] == 'S') {
                        if (soop[nx][ny] == '.' || soop[nx][ny] == 'D') {
                            soop[nx][ny] = 'S';
                            distance[nx][ny] = distance[x][y] + 1;
                            q.offer(new int[]{nx, ny});
                        }
                    } else if (soop[x][y] == '*') {
                        if (soop[nx][ny] == '.' || soop[nx][ny] == 'S') {
                            soop[nx][ny] = '*';
                            q.offer(new int[]{nx, ny});
                        }
                    }
                }
            }
        }
        return "KAKTUS";
    }
}