nums = [-2,1,-3,4,-1,2,1,-5,4]

max_val = float('-inf')
curr_sum = 0
for num in nums:
    curr_sum += num
    if curr_sum > max_val:
        max_val = curr_sum
    if curr_sum < 0:
        curr_sum = 0

print(max_val)