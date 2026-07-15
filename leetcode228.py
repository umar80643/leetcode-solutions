nums = [0,1,2,4,5,7]
l=[]
start= nums[0]
if len(nums)<1:
    print(0)
for i in range(1,len(nums)):
    if nums[i]-nums[i-1]!=1:
        l.append([start,nums[i-1]])
        start=nums[i]
l.append([start,nums[-1]])
ans=[]
for first,second in l:
    if first==second:
        ans.append(str(first))
    else:
        ans.append(f"{first}->{second}")
print(ans)




