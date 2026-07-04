nums = [1,1,1,2,2,3]
if len(nums) <= 2:
    print(nums)
write = 2
for read in range(2, len(nums)):
    if nums[read] != nums[write - 2]:
        nums[write] = nums[read]
        write += 1
print(write)