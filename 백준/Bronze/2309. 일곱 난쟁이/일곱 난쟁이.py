arr = [int(input()) for _ in range(9)]
a = b = 0
tmp=[]
for i in range(8):
    for j in range(i+1, 9):
        if sum(arr) - arr[i] - arr[j] == 100:
            a = arr[i]
            b = arr[j]
tmp.append(a)
tmp.append(b)

for i in tmp:
    arr.remove(i)
    
arr.sort()
for i in arr:
    print(i)