import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.stream.IntStream;

public class Solution {
	private static List<Integer>[] graph;
	
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int T;
		T = 10;
		for (int test_case = 1; test_case <= T; test_case++) {
			String[] s = in.readLine().split(" ");
			int N = Integer.parseInt(s[0]);
			int start = Integer.parseInt(s[1]);
			
			String[] line = in.readLine().split(" ");
			int[] nums = new int[N];
			for (int i = 0; i< N; i++) {
				nums[i] = Integer.parseInt(line[i]);
			}
			
			graph = new ArrayList[101];
			for (int i = 0; i<graph.length; i++) {
				graph[i] = new ArrayList<Integer>();
			}
			
			for (int i = 0; i < N; i+=2) {
				int from = nums[i];
				int to = nums[i+1];
				
				graph[from].add(to);
			}
			
			int result = bfs(start);
			sb.append("#"+test_case+" "+result+"\n");
		}
		
		System.out.println(sb);
	}

	private static int bfs(int start) {
		// TODO Auto-generated method stub
		Queue<int[]> q = new ArrayDeque<>();
		boolean[] visited = new boolean[101];
		
		q.offer(new int[] {start, 0});
		visited[start] = true;
		
		int last_degree = 0;
		int max_num = 0;

		while (!q.isEmpty()) {
			int[] node = q.poll();
			int current = node[0];
			int degree = node[1];
			
			// 가장 큰 번호 찾기
			if (degree > last_degree) {
				last_degree = degree;
				max_num = current;
			} else if (degree == last_degree) {
				max_num = Math.max(current, max_num);
			}
			
			for (int next : graph[current]) {

				if (visited[next] == false) {
					visited[next] = true;
					q.offer(new int[] {next, degree + 1});

				}
			}
		}
		return max_num;
	}
}