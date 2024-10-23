import java.util.*;



class Solution {    
    public List<Integer> solution(String today, String[] terms, String[] privacies) {
        
        List<Integer> answer = new ArrayList<>();

        String[] tds = today.split("\\.");
        int tY = Integer.parseInt(tds[0]);
        int tM = Integer.parseInt(tds[1]);
        int tD = Integer.parseInt(tds[2]);
        
        int idx = 1;
        
        for (String priv : privacies) {

            // privacies, 시작 날짜
            String[] item = priv.split(" ");
            String date = item[0];
            String type = item[1];
            
            String[] startDate = date.split("\\.");
            int year = Integer.parseInt(startDate[0]);
            int month = Integer.parseInt(startDate[1]);
            int day = Integer.parseInt(startDate[2]);

            for (String ty : terms) {
                // terms, 유효기간
                String[] tmp = ty.split(" ");
                String _type = tmp[0];
                int m = Integer.parseInt(tmp[1]);
                
                if (type.equals(_type)) {
                    month += m;
                    break;
                }
            }
            
            year += month/12;
            month = month%12;
            if (month == 0) {
                year -= 1;
                month = 12;
            }
            
            int total = (tY-year)*12*28 + (tM-month)*28 + (tD-day);
            if (total >= 0) {
                answer.add(idx);
            }   
            idx++;
        }

        return answer;
    }
}