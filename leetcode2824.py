nums = [-1,1,2,3,1]
target = 2
count = 0
for i in range(len(nums)):
    j=i+1
    while j<len(nums):
        if nums[i]+nums[j]<target:
            count += 1
        j+=1
print(count)