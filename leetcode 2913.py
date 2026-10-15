nums = [1,2,1]

total = 0
for i in range(len(nums)):
    j=i
    ans=[]
    while j<len(nums):
        if nums[j] not in ans:
            ans.append(nums[j])

        total += len(ans) ** 2
        j +=1

print(total)

