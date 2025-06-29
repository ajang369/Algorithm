t = int(input())
for i in range(t):
    input()
    st_num = int(input())

    candy = 0
    for j in range(st_num):
        candy += int(input())

    if candy % st_num == 0:
        print("YES")
    else:
        print("NO")