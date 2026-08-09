nums = [4,3,2,1]

nums=[0 if x%2==0 else 1 for x in nums]
nums.sort()
print(nums)