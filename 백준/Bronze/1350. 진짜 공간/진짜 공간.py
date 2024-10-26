n = int(input())
file = list(map(int, input().split()))
cler = int(input())

answer = 0

for i in file:
    if i == 0:
        continue
    if i%cler == 0:
        answer += cler*(i//cler)
    else:
        answer += cler*((i//cler)+1)
print(answer)