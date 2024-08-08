import java.util.Scanner;


public class Solution {
	public static int recursionNum(int n, int cnt) {
		if (cnt == 1)
			return n;
		
		return n * recursionNum(n, cnt-1);
	}
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = 10;
		for(int test_case = 1; test_case <= T; test_case++) {
			int t = sc.nextInt();
			int num = sc.nextInt();
			int cnt = sc.nextInt();

			int result = recursionNum(num, cnt);
			
			System.out.println("#"+test_case+" "+result);
		}
		
		sc.close();
	}
}