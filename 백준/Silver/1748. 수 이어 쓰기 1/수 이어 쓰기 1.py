n=input()
length = len(n)

result = 0
for i in range(length-1):
    result += 9*(10**i) * (i+1)
tmp = int(n) - (10**(length-1))
result += (tmp+1)*length

print(result)