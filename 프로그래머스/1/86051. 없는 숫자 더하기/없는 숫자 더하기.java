class Solution {
    public int solution(int[] numbers) {
        int sum = 0;
        for (int i = 0; i < 10; i++) {
            sum += i;
        }
        for (int n : numbers) {
            sum -= n;
        }
        
        return sum;
        
    }
}