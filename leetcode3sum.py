nums = [-1,0,1,2,-1,-4]
nums.sort()


sum = 0
for i in range(0,len(nums)):
    if i>0 and nums[i]==nums[i-1]:
        continue
    l = i+1
    r = len(nums)-1
    while l < r:
        sum = nums[i] + nums[l] + nums[r]

        if sum == 0:
            print([nums[i] , nums[l] , nums[r]])
            l = l + 1
            r = r - 1
            while l<r and nums[l] == nums[l-1]:
                l = l + 1
            while l<r and nums[r] == nums[r+1]:
                r = r - 1
        elif sum<0:
            l = l + 1
        else:
            r = r - 1

