nums = [3, 2, 2, 3]
val = 3
i = 0
for k in range(len(nums)):
    if nums[k]!=val:
        nums[i]=nums[k]
        i+=1
print(i)