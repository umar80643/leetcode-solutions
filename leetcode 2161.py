nums = [9,12,5,10,14,3,10]
pivot = 10

n=len(nums)
ans=[0]*n

l=0
r=n-1

for num in nums:
    if num<pivot:
        ans[l]=num
        l+=1
for num in reversed(nums):
    if num>pivot:
        ans[r]=num
        r-=1
while l<=r:
    ans[l]=pivot
    l+=1

print(ans)