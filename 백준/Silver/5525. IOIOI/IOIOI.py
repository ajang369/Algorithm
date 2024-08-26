n = int(input())
m = int(input())
S = input()

pn_len = n*2 + 1

tmp = ''
for i in range(pn_len):
    if i%2 == 0:
        tmp += 'I'
    else:
        tmp += 'O'

cnt = 0
for i in range(m):
    if S[i] == 'I':
        res = S[i:i+pn_len]
        if res == tmp:
            cnt += 1
print(cnt)