nums = [3,2,1]
k = 1

for i in range(len(nums)):
    max_val= max(nums[:i+1])
    min_val= min(nums[i:])
    if max_val - min_val <=k:
        print(i)
        break
print(-1)