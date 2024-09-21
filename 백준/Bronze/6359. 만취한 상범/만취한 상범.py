t = int(input())

for _ in range(t):
    n = int(input())

    room = [1] * (n+1)

    for i in range(2, n+1):
        k = i

        while k <= n:
            room[k] *= -1
            k += i

    res = room.count(1)
    print(res - 1)