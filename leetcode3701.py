nums = [1,3,5,7]
total = 0
for i in range(len(nums)):
    if i % 2 == 0:
        total+=nums[i]
    else:
        total-=nums[i]
print(total)