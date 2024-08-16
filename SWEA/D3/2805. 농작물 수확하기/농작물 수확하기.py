
T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    farm = []
    for _ in range(N):
        farm.append(list(map(int, input())))

    center = N//2
    total = 0
    # 한 줄씩
    for i in range(N):
        start = abs(center - i)

        if i <= center:
            end_col = center + i
            total += sum(farm[i][start:end_col + 1])
        else:
            end = center + ((N - 1) - i)
            total += sum(farm[i][start:end + 1])

    print(f'#{test_case} {total}')