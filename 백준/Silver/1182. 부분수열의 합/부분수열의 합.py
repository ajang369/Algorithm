N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

def dfs(idx, sum):
    global cnt

    if (idx >= N):
        return
    
    sum += nums[idx]
    if sum == S:
        cnt += 1

    dfs(idx+1, sum)
    dfs(idx+1, sum-nums[idx])

dfs(0,0)
print(cnt)