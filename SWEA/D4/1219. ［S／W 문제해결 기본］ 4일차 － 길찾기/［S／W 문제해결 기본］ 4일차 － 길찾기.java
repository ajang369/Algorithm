import java.util.*;
import java.io.*;

public class Solution {
	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int T = 10;
		for(int test_case = 1; test_case <= T; test_case++)
		{
			sb.append("#" + test_case + " ");
//			int t = Integer.parseInt(line[0]);
//			int way = Integer.parseInt(line[1]);

			int[][] graph = new int[100][100];
			boolean[] visited = new boolean[100];

			String line = in.readLine();

			String[] s = in.readLine().split(" ");
			int[] numList = new int[s.length];

			for (int i = 0; i < s.length; i++) {
				numList[i] = Integer.parseInt(s[i]);
			}

			for (int i = 0; i < s.length; i+=2) {
				int u = numList[i];
				int v = numList[i+1];
				graph[u][v] = 1;
			}

			int start = 0;
			int end= 99;

			boolean isValid = dfs(graph, start, end, visited);
			if (isValid) {
				sb.append("1" + "\n");
			} else {
				sb.append("0" + "\n");
			}
		}
		System.out.println(sb);
	}

	private static boolean dfs(int[][] graph, int current, int target, boolean[] visited) {
		if (current == target)
			return true;

		visited[current] = true;

		for (int i = 0; i < 100; i++) {
			// 현재 탐색하고 있는 점과 연결되어 있으면서 방문하지 않은 점 일 때
			if (graph[current][i] == 1 && visited[i] == false) {
				boolean res = dfs(graph, i, target, visited);
				if (res) {
					return true;
				}
			}
		}

		return false;
	}
}