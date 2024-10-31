st = input()

cnt1 = 0
cnt2 = 0

ex = st.split('.')
flag = True

res = []

for i in range(len(ex)):
    if ex[i] != '' and ex[i][0] != '.':
        if len(ex[i])%2 == 0:
            tmp = (len(ex[i]) // 4) * 'AAAA' + (len(ex[i]) % 4) * 'B'
            ex[i] = tmp
        else:
            flag = False
            break

for i in range(1, len(ex)):
    ex[i] = '.' + ex[i]

if flag:
    answer = ''.join(ex)
    print(answer)
else:
    print(-1)