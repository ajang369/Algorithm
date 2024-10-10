import math

N = int(input())
nums = list(map(int, input().split()))

for i in range(1, N):
    A = nums[0]
    B = nums[i]
    tmp = math.gcd(A, B)
    result = f'{A//tmp}/{B//tmp}'
    print(result)