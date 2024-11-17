n, k = map(int, input().split())
A = list(map(int, input().split()))
flag = True
cnt = 0
for i in range(1, n):
    # 크기가 이미 앞에 있는 것 보다 크면 넘어감
    if A[i-1] < A[i]:
        continue

    # 같거나 더 작은 경우 k 더해줌
    A[i] += k
    # 더하고 난 상태 비교
    # 이 전 숫자가 더 크거나 같을 때는 불가능한 경우
    if A[i-1] >= A[i]:
        flag = False
        break
    cnt += 1    # 횟수 더함

if flag:
    print(cnt)
else:
    print(-1)