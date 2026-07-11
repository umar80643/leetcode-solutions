nums = [3, 4, -1, 1]
n = len(nums)
i =0
while i < n:
    correct_index = nums[i] - 1
    if nums[i] > 0 and nums[i] <= n and nums[i] != nums[correct_index]:
        nums[i] , nums[correct_index] = nums[correct_index] , nums[i]

    else:
        i += 1
for i in range(n):
    if nums[i]!=i+1:
        print(i+1)
        break
print(n+1)