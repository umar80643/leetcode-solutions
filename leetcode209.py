target = 7
nums = [2,3,1,2,4,3]
min_length = float("inf")
left = 0
curr_sum = 0

for i in range(len(nums)):
    curr_sum += nums[i]
    while curr_sum >= target:
        min_length = min(min_length, i - left + 1)
        curr_sum -= nums[left]
        left += 1


print(min_length)