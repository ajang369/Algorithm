s = input()
answer = ''
for i in s:
    if i.islower():
        res = chr(97 + (ord(i)+13-97)%26)
        answer += res
    elif i.isupper():
        res = chr(65 + (ord(i)+13-65)%26)
        answer += res
    else:
        answer += i
print(answer)