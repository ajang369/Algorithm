T = int(input())
for _ in range(T):
    n = int(input())
    result = 0

    for i in range(n):
        li = list(map(int, input().split()))
        _max = max(li)
        if _max < 0:
            continue
        result += _max
    print(result)