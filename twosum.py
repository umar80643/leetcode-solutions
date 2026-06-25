nums = [2,7,11,13,15]
target = 9
d={}
for i in range(len(nums)-1):
    need = target - nums[i]
    if need in d:
        print(d[need],i)
    else:
        d[nums[i]]=i
