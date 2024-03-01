n1,n2 = map(int, input().split())
fir = list(input())
sec = list(input())
t=int(input())
ant = fir[::-1] + sec
for _ in range(t):
    for i in range(n1+n2-1):
        if (ant[i] in fir) and (ant[i+1] in sec):
            ant[i], ant[i+1] = ant[i+1], ant[i]
            if fir[0] == ant[i+1]:
                break
print(''.join(ant))