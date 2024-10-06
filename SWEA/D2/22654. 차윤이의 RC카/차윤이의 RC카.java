import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Solution {
    static int[] dx = {-1, 0, 1, 0}; // 상, 우, 하, 좌
    static int[] dy = {0, 1, 0, -1}; // 상, 우, 하, 좌

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());  // 테스트 케이스 수

        for (int t = 1; t <= T; t++) {
            int N = Integer.parseInt(br.readLine());  // 필드 크기
            char[][] field = new char[N][N];

            int startX = 0, startY = 0;
            int targetX = 0, targetY = 0;

            // 필드 정보 입력
            for (int i = 0; i < N; i++) {
                String row = br.readLine();
                for (int j = 0; j < N; j++) {
                    field[i][j] = row.charAt(j);
                    if (field[i][j] == 'X') {
                        startX = i;
                        startY = j;
                    } else if (field[i][j] == 'Y') {
                        targetX = i;
                        targetY = j;
                    }
                }
            }

            int Q = Integer.parseInt(br.readLine());  // 조종 횟수
            sb.append("#").append(t).append(" ");  // 테스트 케이스 번호 출력

            // 각 커맨드 처리
            for (int q = 0; q < Q; q++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int C = Integer.parseInt(st.nextToken());  // 커맨드 길이
                String commands = st.nextToken();  // 커맨드 문자열

                // 초기 위치 및 방향 설정
                int x = startX;
                int y = startY;
                int dir = 0;  // 0: 위, 1: 오른쪽, 2: 아래, 3: 왼쪽

                for (int i = 0; i < C; i++) {
                    char command = commands.charAt(i);

                    if (command == 'L') {
                        dir = (dir + 3) % 4;  // 왼쪽으로 회전
                    } else if (command == 'R') {
                        dir = (dir + 1) % 4;  // 오른쪽으로 회전
                    } else if (command == 'A') {
                        int nx = x + dx[dir];
                        int ny = y + dy[dir];

                        // 필드를 벗어나지 않고, 나무가 없는 경우에만 이동
                        if (nx >= 0 && nx < N && ny >= 0 && ny < N && field[nx][ny] != 'T') {
                            x = nx;
                            y = ny;
                        }
                    }
                }

                // 마지막 위치가 목표 지점인지 확인
                if (x == targetX && y == targetY) {
                    sb.append("1 ");
                } else {
                    sb.append("0 ");
                }
            }
            sb.append("\n");
        }

        // 결과 출력
        System.out.print(sb.toString());
    }
}