nums=[10,4,8,3]


leftSum=[0]
rightSum=[0]*len(nums)

total1=0
for i in range(len(nums)-1):
    total1+=nums[i]
    leftSum.append(total1)
print(leftSum)

total2=0
for i in range(len(nums)-1,-1,-1):
    rightSum[i]=total2
    total2+=nums[i]
print(rightSum)

l=0
r=0
ans=[]
while l<len(leftSum) and r<len(rightSum):
    total=abs(leftSum[l]-rightSum[r])
    ans.append(total)
    l+=1
    r+=1
print(ans)







