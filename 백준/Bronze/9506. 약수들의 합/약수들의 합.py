while True:
    n = int(input())
    if n == -1:
        break
    li = []
    flag = False
    
    for i in range(1, n):
        if n%i == 0:
            li.append(i)
    if n == sum(li):
        flag = True
    
    if flag:
        print(f'{n} = ', end="")
        print(' + '.join(map(str, li)))
    else:
        print(f'{n} is NOT perfect.')