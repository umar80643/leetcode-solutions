nums = [2,3,4]
xor =0
has_zero = False
for i in range(0,len(nums)):
        xor  ^= nums[i]
        if nums[i] != 0:
            has_zero = True
if xor != 0:
    print(len(nums))
if has_zero:
    print(len(nums)-1)
else:
    print(0)