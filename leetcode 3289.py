nums = [0,1,1,0]
d={}
for num in nums:
    if num in d:
        d[num]+=1
    else:
        d[num]=1
ans=[]
for key,values in d.items():
     if values >1:
           ans.append(key)
print(ans)