def cut(n):
    if n == 1:
        return '-'
    else:
        left = cut(n//3)
        center = " " * (n//3)

        return left + center + left


while True:
    try:
        n = int(input())
        print(cut(3**n))
    except:
        break