n, k = map(int, input().split())
kid = list(map(int, input().split()))

charge = []
for i in range(1, n):
    charge.append(kid[i]-kid[i-1])
charge.sort(reverse=True)
print(sum(charge[k-1:]))