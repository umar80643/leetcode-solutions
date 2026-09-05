nums = [5,0,1,4]
k = 3


n = len(nums)

suffix_min = [0] * n
suffix_min[-1] = nums[-1]

for i in range(n - 2, -1, -1):
    suffix_min[i] = min(nums[i], suffix_min[i + 1])

max_val = nums[0]

for i in range(n):
    max_val = max(max_val, nums[i])

    if max_val - suffix_min[i] <= k:
        return i

return -1