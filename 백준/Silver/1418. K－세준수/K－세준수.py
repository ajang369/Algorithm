import math

N = int(input())
K = int(input())

# 소수 먼저 구하기
sosu = [True] * (100001)

# 에라토스테네스의 체를 사용해서 소수인 것만 True로
for i in range(2, int(math.sqrt(100000))+1):
    if sosu[i]:
        j = 2
        while i*j <= 100000:
            sosu[i*j] = False
            j += 1

# 인덱스가 k-세준수이면 1, 아니면 0
k_num = [1]*(N+1)
k_num[0] = 0
for i in range(2, N+1):
    # K보다 큰 소수의 배수들을 제외
    if sosu[i] and i > K:
        for j in range(i, N+1, i):
            k_num[j] = 0

print(sum(k_num))