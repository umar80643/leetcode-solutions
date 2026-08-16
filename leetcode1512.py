nums = [1,1,1,1]
pair =0
for i in range(0,len(nums)):
    j=i+1
    while j<len(nums):
        if nums[j]==nums[i] and i<j:
            pair += 1
        j+=1
print(pair)
