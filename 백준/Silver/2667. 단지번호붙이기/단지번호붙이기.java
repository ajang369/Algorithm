import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
	
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	static int[][] map;
	static boolean[][] visited;
	static int num;
	static List<Integer> danji;
	static int count;

	public static void main(String[] args) throws Exception{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		map = new int[N][N];
		visited = new boolean[N][N];
		danji = new ArrayList<>();
		
		for (int i = 0; i < N; i++) {
			String[] line = in.readLine().split("");
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(line[j]);
			}
		}
		
		num = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j] && map[i][j] == 1) {
					count = 0;
					dfs(i, j);
					danji.add(count);
					num += 1;
				}
			}
		}
		
		Collections.sort(danji);
		
		System.out.println(num);
		for (int i : danji) {
			System.out.println(i);
		}
	}
	
	static void dfs(int x, int y) {
		
		visited[x][y] = true;
		count++;
		
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			
			if (nx >= 0 && ny >= 0 && nx < map.length && ny < map.length && !visited[nx][ny] && map[nx][ny] == 1) {
				dfs(nx, ny);
			}
		}
	}
}