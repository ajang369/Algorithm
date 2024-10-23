import java.util.*;

public class Main {
	static int N, M;
	static int[][] directions = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
	static int maxSafeArea = 0;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();

		int[][] startArr = new int[N][M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				startArr[i][j] = sc.nextInt();
			}
		}

		virusGame(startArr);

	}

	private static void virusGame(int[][] startArr) {
		List<int[][]> result = new ArrayList<>();

		// 1. 빈 칸 중 3개의 위치를 조합으로 선택
		combinations(startArr, result);

		for (int[][] walls : result) {
			int[][] tempArr = new int[N][M];
			for (int i = 0; i < N; i++) {
				tempArr[i] = startArr[i].clone(); // 복사
			}

			// 2. 선택된 빈 칸에 벽 세우기
			for (int[] wall : walls) {
				tempArr[wall[0]][wall[1]] = 1;
			}

			// 3. 바이러스 퍼뜨리기
			spreadVirus(tempArr);

			// 4. 안전한 칸 세기
			int safeArea = countSafeArea(tempArr);

			maxSafeArea = Math.max(maxSafeArea, safeArea);
		}

		System.out.println(maxSafeArea);

	}

	private static int countSafeArea(int[][] tempArr) {
		int safe = 0;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (tempArr[i][j] == 0) {
					safe++;
				}
			}
		}
		return safe;
	}

	private static void spreadVirus(int[][] map) {
		Queue<int[]> queue = new LinkedList<>();

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] == 2) {
					queue.add(new int[] { i, j });
				}
			}
		}

		while (!queue.isEmpty()) {
			int[] current = queue.poll();
			int x = current[0];
			int y = current[1];

			for (int[] dir : directions) {
				int nx = x + dir[0];
				int ny = y + dir[1];

				if (nx >= 0 && ny >= 0 && nx < N && ny < M && map[nx][ny] == 0) {
					map[nx][ny] = 2;
					queue.add(new int[] { nx, ny });
				}
			}
		}

	}

	private static void combinations(int[][] startArr, List<int[][]> result) {
		List<int[]> empty = new ArrayList<>();

		for (int i = 0; i < startArr.length; i++) {
			for (int j = 0; j < startArr[0].length; j++) {
				if (startArr[i][j] == 0) {
					empty.add(new int[] { i, j });
				}
			}
		}

		combineWalls(empty, new int[3][2], 0, 0, result);

	}

	private static void combineWallsHelper(List<int[]> empty, int[][] selectedWalls, int start, int depth,
			List<int[][]> result) {
		if (depth == 3) {
			int[][] com = new int[3][2];
			for (int i = 0; i < 3; i++) {
				com[i][0] = selectedWalls[i][0];
				com[i][1] = selectedWalls[i][1];
			}

			result.add(com);
			return;
		}

	}

	private static void combineWalls(List<int[]> empty, int[][] selectedWalls, int start, int depth,
			List<int[][]> result) {
		if (depth == 3) {
			int[][] combination = new int[3][2];
			for (int i = 0; i < 3; i++) {
				combination[i][0] = selectedWalls[i][0];
				combination[i][1] = selectedWalls[i][1];
			}

			result.add(combination);
			return;
		}

		for (int i = start; i < empty.size(); i++) {
			selectedWalls[depth] = empty.get(i);
			combineWalls(empty, selectedWalls, i + 1, depth + 1, result);
		}

	}

}