import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;

public class Solution {

	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
//		System.setIn(new FileInputStream("res/input.txt"));
		
		int T = 10;
		for(int test_case = 1; test_case <= T; test_case++)
		{
			sb.append("#" + test_case + " ");
			String[] line = in.readLine().split(" ");
			Stack<Integer> stack = new Stack<>();
			
			int N = Integer.parseInt(line[0]);
			String num = line[1];
			String[] tmp = num.split("");
			int[] numLi = new int[N];
			for (int i = 0; i < N; i++) {
				numLi[i] = Integer.parseInt(tmp[i]);
			}
			
			for (int i = 0; i < N; i++) {
				if (!stack.isEmpty()) {
					if (stack.peek() != numLi[i]) {
						stack.push(numLi[i]);
					} else {
						stack.pop();
					}
				} else {
					stack.push(numLi[i]);
				}
			}
			int size = stack.size();
			int[] res = new int[size];
			for (int i = 0; i < size; i++) {
				res[i] = stack.pop();
			}

			int[] reverse = new int[size];
			for (int j = res.length-1, i = 0; j>=0; j--, i++) {
				reverse[i] = res[j];
			}
			for (int i = 0; i< size; i++) {
				sb.append(reverse[i]);
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}
}