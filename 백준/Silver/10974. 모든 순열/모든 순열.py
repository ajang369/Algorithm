import itertools

N=int(input())
li = [i for i in range(1, N+1)]

result = list(itertools.permutations(li, N))
result.sort()
for nums in result:
    print(*nums)