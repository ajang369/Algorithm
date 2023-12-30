import math
nums = list(map(int, input().split()))
res_lcm = []
for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            res_lcm.append(math.lcm(nums[i], nums[j], nums[k]))
print(min(res_lcm))