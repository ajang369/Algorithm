n=int(input())
li = list(map(int, input().split()))
count = 0
for i in range(n):
    if li[i] in li[:i]:
        count += 1
print(count)