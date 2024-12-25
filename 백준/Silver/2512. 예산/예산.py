n = int(input())
cost = list(map(int, input().split()))
limit = int(input())

lo = 1
hi = int(1e9)


def check(mid):
    sum = 0
    for c in cost:
        if c <= mid:
            sum += c
        else:
            sum += mid

    if sum <= limit:
        return 1


if sum(cost) <= limit:
    print(max(cost))
else:
    while (lo + 1 < hi):
        mid = (lo + hi) // 2

        if check(mid):
            lo = mid
        else:
            hi = mid

    print(lo)