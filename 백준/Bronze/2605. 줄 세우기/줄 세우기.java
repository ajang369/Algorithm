import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		List<Integer> result = new ArrayList<>();


		for (int i = 0; i < N; i++) {
			int n = sc.nextInt();
			
			result.add(result.size() - n, i+1);
		}
		
		for (int i = 0; i < N; i++) {
			System.out.print(result.get(i) + " ");
		}
	}
}