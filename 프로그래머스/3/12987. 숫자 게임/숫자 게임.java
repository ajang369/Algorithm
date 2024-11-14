import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        Arrays.sort(A);
        Arrays.sort(B);
        
        int idxA = A.length - 1;
        int idxB = B.length - 1;
        int answer = 0;
        
        for (int i = 0; i < A.length; i++) {
            if (A[idxA] < B[idxB]) {
                answer++;
                idxA--;
                idxB--;
            } else {
                idxA--;
            }
        }
        return answer;
    }
}