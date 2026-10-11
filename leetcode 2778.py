nums = [1,2,3,4]

n = len(nums)

ans = 0
j=1
for i in range(1,n+1):
    if n % i ==0:
        ans += nums[i-1]*nums[i-1]


print(ans)