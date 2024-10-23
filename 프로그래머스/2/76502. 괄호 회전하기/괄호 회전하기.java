import java.util.Stack;

class Solution {
    public int solution(String s) {
        int length = s.length();
        int result = 0;

        for (int i = 0; i < length; i++) {
            if (isValid(s)) {
                result++;
            }
            // 회전
            s = rotateLeft(s);
        }

        return result;
    }

    private boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (char ch : s.toCharArray()) {
            if (ch == '[' || ch == '(' || ch == '{') {
                stack.push(ch);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                char top = stack.pop();
                if (!isMatchingPair(top, ch)) {
                    return false;
                }
            }
        }
        
        return stack.isEmpty();
    }

    private boolean isMatchingPair(char open, char close) {
        return (open == '[' && close == ']') ||
               (open == '(' && close == ')') ||
               (open == '{' && close == '}');
    }

    private String rotateLeft(String s) {
        return s.substring(1) + s.charAt(0);
    }
}
