nums = [2,10,7,5,4,1,8,6]

n = len(nums)

min_ind = nums.index(min(nums))
max_ind = nums.index(max(nums))



left = min(min_ind, max_ind)
right = max(min_ind, max_ind)

print(min(
    right + 1,           #
    n - left,
    left + 1 + n - right
))







