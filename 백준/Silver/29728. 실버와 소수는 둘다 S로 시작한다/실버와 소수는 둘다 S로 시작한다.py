from collections import deque

N = int(input())

A = deque()
A.append('B')

arr = [True] * (N+1)

is_reverse = True   # 뒤집는거 고려한 조건

# 에라토스테네스 체
for i in range(2, int(N**(0.5)) + 1):
    if arr[i] == True:
        j = 2
        while i*j <= N:
            arr[i*j] = False
            j += 1

for i in range(2, N+1):
    if arr[i] == True: # 소수인경우
        if is_reverse == True:  # 안 뒤집음


            # 마지막 문자가 B일 때
            if A[-1] == 'B':  # S로 교체하고 S 추가
                A.pop()
                A.append('S')
                A.append('S')
            # 아니면 그냥 S 추가, 뒤집기
            else:
                A.append('S')
                is_reverse = not is_reverse

        else:   # 뒤집음
            if A[0] == 'B':  # 맨 앞을 S로 교체하고 앞에 S 추가
                A.popleft()
                A.appendleft('S')
                A.appendleft('S')
            # 아니면 그냥 S 추가
            else:
                A.appendleft('S')
                is_reverse = not is_reverse

    # 소수 아니면
    else:
        if is_reverse == True:
            A.append('B')
        else:
            A.appendleft('B')

print(A.count('B'), A.count('S'))