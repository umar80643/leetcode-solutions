nums = [3,4,5,1,12,14,13]
ans = nums[0]
for i in range(1,len(nums)):
    if nums[i-1]+1==nums[i]:
        ans += nums[i]
    else:
        break

s =set(nums)
while ans in s:
    ans +=1
print(ans)