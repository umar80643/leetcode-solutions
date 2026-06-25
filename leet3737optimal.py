nums = [1,2,2,3]
target = 2
ans =0
for i in range(0,len(nums)):
    freq =0
    for j in range(i,len(nums)):
        if nums[j]==target:
            freq+=1
        length = j-i+1
        if freq>length//2:
            ans+=1
print(ans)
