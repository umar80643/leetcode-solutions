nums = [1, 2, 3, 1, 2, 3]
k = 2
d={}
for i in range(len(nums)):
    if nums[i] in d:
        if i - d[nums[i]] <= k:
            print(True)
        else:
            d[nums[i]] = i

    else:
        d[nums[i]]=i
print(False)