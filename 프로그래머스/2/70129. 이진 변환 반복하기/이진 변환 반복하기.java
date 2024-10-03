public class Solution {
    public int[] solution(String s) {
        int cnt = 0;        // 변환 횟수
        int zeroCnt = 0;    // 0의 개수

        while (!s.equals("1")) { // s가 1이 될 때까지 반복
            int initLen = s.length();
            s = s.replace("0", "");
                
            zeroCnt += initLen - s.length();

            s = Integer.toBinaryString(s.length());
            cnt++;
        }

        return new int[]{cnt, zeroCnt};
    }
}
