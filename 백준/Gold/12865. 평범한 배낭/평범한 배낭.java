import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());	// 버틸 수 있는 무게 K
		
		int[] dp = new int[100001];
		
		int[] weight = new int[N];
		int[] value = new int[N];
		for (int i = 0; i<N; i++) {
			// 무게 w, 가치 v
			st = new StringTokenizer(br.readLine());
			int w = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			weight[i] = w;
			value[i] = v;
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = K; j >= weight[i]; j--) {
				dp[j] = Math.max(dp[j], dp[j - weight[i]] + value[i]);
			}
		}
		sb.append(dp[K]);
		
		System.out.println(sb);
	}
	

}