nums = [2, 3, -1, 8, 4]
left_sum = 0
total_sum = sum(nums)
for i in range(len(nums)):
    right_sum = total_sum - left_sum - nums[i]
    if left_sum == right_sum:
        print(i)
        break
    left_sum += nums[i]

print(-1)