code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        tmp = list(map(int, input()))
        arr.append(tmp)

    end = 0
    cnt = 0
    pw = []
    for line in arr:
        for i in range(m-1, -1, -1):
            if line[i] == 1:
                end = i
                start = end - 55
                pw = line[start:end+1]
                break

    res = 0

    passwd = []
    for i in range(0, 56, 7):
        tmp = ''.join(map(str, pw[i:i+7]))
        passwd.append(tmp)
    numbers = []
    for p in passwd:
        num = code.index(p)
        numbers.append(num)
    hol, jak = 0, 0
    for i in range(0, 8, 2):
        hol += numbers[i]
        jak += numbers[i+1]
    check = hol*3 + jak
    if check % 10 == 0:
        res = sum(numbers)
    print(f'#{test_case} {res}')

