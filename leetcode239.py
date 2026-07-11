nums = [1,3,-1,-3,5,3,6,7]
k = 3
i=0
j=0
l=[]
ans =[]
maxNum=float('-inf')
while i<len(nums)+1:
    if i-j<k:
        l.append(nums[i])
        i+=1
    if i-j==k:
        ans.append(max(l))
        l.remove(nums[j])
print(maxNum)








