public class Solution {
    public int[] solution(String s) {
        int cnt = 0;
        int zeroCnt = 0;

        while (!s.equals("1")) {
            zeroCnt += s.length() - s.replace("0", "").length();
            s = s.replace("0", "");
            s = Integer.toBinaryString(s.length());
            cnt++;
        }

        return new int[]{cnt, zeroCnt};
    }
}
