import java.util.*;

class Solution {

    // 순열 생성 메서드
    public static List<List<String>> getPermutations(List<String> userIds, int n) {
        List<List<String>> permutations = new ArrayList<>();
        generatePermutations(userIds, new ArrayList<>(), permutations, n);
        return permutations;
    }

    // 순열을 생성하는 재귀 함수
    private static void generatePermutations(List<String> userIds, List<String> current, List<List<String>> result, int n) {
        if (current.size() == n) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (String userId : userIds) {
            if (!current.contains(userId)) {  // 중복 방지
                current.add(userId);
                generatePermutations(userIds, current, result, n);
                current.remove(current.size() - 1);
            }
        }
    }

    // solution 메서드
    public static int solution(String[] user_id, String[] banned_id) {
        // 배열을 List로 변환
        List<String> userIds = Arrays.asList(user_id);
        List<String> bannedIds = Arrays.asList(banned_id);

        int n = bannedIds.size();  // 밴 아이디 개수
        List<List<String>> permutations = getPermutations(userIds, n);  // 순열 구하기
        
        Set<Set<String>> answer = new HashSet<>();  // 중복을 제거하기 위해 Set 사용
        
        // 모든 순열을 탐색
        for (List<String> perm : permutations) {
            boolean isMatch = true;  // 가능 여부
            
            // 선택한 유저 아이디와 밴 아이디 비교
            for (int i = 0; i < n; i++) {
                String u = perm.get(i);  // 유저 ID
                String b = bannedIds.get(i);  // 밴 ID
                
                // 두 아이디 길이가 같을 때만 비교
                if (u.length() == b.length()) {
                    for (int j = 0; j < u.length(); j++) {
                        // 밴 아이디에 '*' 있으면 스킵
                        if (b.charAt(j) == '*') continue;
                        // 서로 다른 문자면 일치하지 않음
                        if (u.charAt(j) != b.charAt(j)) {
                            isMatch = false;
                            break;
                        }
                    }
                } else {
                    isMatch = false;  // 길이가 다르면 불가능
                    break;
                }

                if (!isMatch) break;
            }

            // 가능한 경우에 중복 체크
            if (isMatch) {
                Set<String> permSet = new HashSet<>(perm);  // 순서를 무시하기 위해 Set 사용
                answer.add(permSet);  // 중복을 제거하며 추가
            }
        }
        
        return answer.size();  // 가능한 경우의 수 반환
    }
}