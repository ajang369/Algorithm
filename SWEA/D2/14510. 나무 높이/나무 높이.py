
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))
    high = max(li)
    hol = 0     # 홀수 날
    jak = 0     # 짝수 날
    res = 0     # 결과값

    for height in li:
        diff = high - height
        hol += diff % 2
        jak += diff // 2

    if hol <= jak:

        res += hol*2
        jak -= hol
        day = jak*2
        res += ((day // 3) * 2) + (day % 3)
    else:
        res += hol*2 - 1
    print(f'#{test_case} {res}')