import sys
input = sys.stdin.readline
while 1:
    a, b, c = map(int, input().split())
    li=[]
    li.append(a)
    li.append(b)
    li.append(c)
    li.sort()
    if a == b == c == 0:
        break

    if li[2] >= li[0]+li[1]:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")