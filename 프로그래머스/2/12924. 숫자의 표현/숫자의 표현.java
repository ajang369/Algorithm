class Solution {
    public static int solution(int n) {
		int cnt = 0;

		for (int i = 0; i < n; i++) {
			int sum = 0;
			
			for (int j = i; j < n; j++) {
				sum += j + 1;
				
				if(sum == n) {
					cnt++;
					break;
				} else if(sum > n) {
					break;
				}
			}
		}		

		return cnt;
	}
}