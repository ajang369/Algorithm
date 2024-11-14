def is_cute(s):
    # '+'가 하나 있고, 그 위치를 찾는다
    if s.count('+') != 1:
        return "No Money"
    
    left, right = s.split('+')
    
    # 양쪽 모두 양의 정수 형태인지 확인 (0으로 시작하지 않아야 함)
    if not (left.isdigit() and right.isdigit()):
        return "No Money"
    if left[0] == '0' or right[0] == '0':
        return "No Money"
    
    # 왼쪽과 오른쪽 숫자가 같은지 확인
    if left == right:
        return "CUTE"
    else:
        return "No Money"

# 예시 입력
s = input().strip()
print(is_cute(s))