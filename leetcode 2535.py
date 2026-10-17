nums = [1,15,6,3]

ans_sum = sum(nums)

ans_total =0
for num in nums:
    while num>0:
        r = num%10
        ans_total += r
        num //= 10
print(abs(ans_sum-ans_total))
