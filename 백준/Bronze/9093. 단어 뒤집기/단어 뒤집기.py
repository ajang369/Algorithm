n=int(input())
for _ in range(n):
    s = list(map(str, input().split()))
    tmp = []
    for i in range(len(s)):
        tmp.append(s[i][::-1])
    print(' '.join(tmp))