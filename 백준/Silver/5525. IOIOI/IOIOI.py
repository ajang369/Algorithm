n = int(input())
m = int(input())
S = input()

idx, count = 0, 0
result = 0
while idx < (m-1):
    # idx부터 길이가 3인곳 까지 IOI인지 확인
    if S[idx:idx+3] == 'IOI':
        count += 1
        idx += 2    # 다음으로 이동 -> +2


        if count == n:
            result += 1
            count -= 1
    else:
        idx += 1
        count = 0
print(result)