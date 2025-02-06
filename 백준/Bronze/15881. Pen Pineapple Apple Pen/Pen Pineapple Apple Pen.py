order = 'pPAp'
count =0
i = 0

n = int(input())
words = input()

while i != n:
    if words[i:i+4] == order:
        count +=1
        i = i +4
    else:
        i +=1
print(count)