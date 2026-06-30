nums = [0,0,1,1,1,2,2,3,3,4]
write = 1
for read in range(1,len(nums)):
    if nums[read]!= nums[write-1]:
        nums[write] = nums[read]
        write += 1

print(write)