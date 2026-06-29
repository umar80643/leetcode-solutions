nums = [3,-1]

min_val = min(nums)
max_val = max(nums)

count = [0]*(max_val-min_val+1)

for num in nums:
    count[num-min_val] += 1
nums.clear()
for i in range(0,len(count)):
    nums.extend([i+min_val]*count[i])
print(nums)
