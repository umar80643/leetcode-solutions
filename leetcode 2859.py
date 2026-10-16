nums = [5,10,1,5,2]
k = 1
ans=0
for i in range(len(nums)):
    binary = str(bin((i)))[2::]
    if binary.count('1')== k:
        ans += nums[i]

print(ans)





