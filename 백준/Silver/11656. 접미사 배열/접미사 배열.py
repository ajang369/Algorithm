s=input()
li = []
for i in range(len(s)):
    tmp = s[i:]
    li.append(tmp)
li.sort()
for i in li:
    print(i)