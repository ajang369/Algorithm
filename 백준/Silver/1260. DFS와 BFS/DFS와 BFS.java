import java.util.*;

public class Main {

    private static List<Integer>[] graph;
    private static boolean[] visited;
    private static List<Integer> res_dfs = new ArrayList<>();
    private static List<Integer> res_bfs = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int v = sc.nextInt();

        graph = new ArrayList[n + 1];
        visited = new boolean[n + 1];

        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph[a].add(b);
            graph[b].add(a);
        }

        for (int i = 1; i <= n; i++) {
            Collections.sort(graph[i]);
        }

        // DFS 탐색
        dfs(v);

        // BFS 탐색을 위해 visited 배열 초기화
        Arrays.fill(visited, false);

        // BFS 탐색
        bfs(v);

        // 결과 출력
        for (int num : res_dfs) {
            System.out.print(num + " ");
        }
        System.out.println();

        for (int num : res_bfs) {
            System.out.print(num + " ");
        }
    }

    private static void dfs(int start) {
        res_dfs.add(start);
        visited[start] = true;

        for (int i : graph[start]) {
            if (!visited[i]) {
                dfs(i);
            }
        }
    }

    private static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        visited[start] = true;
        q.offer(start);

        while (!q.isEmpty()) {
            int node = q.poll();
            res_bfs.add(node);

            for (int i : graph[node]) {
                if (!visited[i]) {
                    visited[i] = true;
                    q.offer(i);
                }
            }
        }
    }
}