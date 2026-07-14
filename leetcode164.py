nums = [3,6,9,1]
nums.sort()
max_diff = float('-inf')
if len(nums) < 2:
    print(0)

for i in range(1, len(nums)):
    max_diff = max(max_diff, nums[i] - nums[i - 1])
print(max_diff)