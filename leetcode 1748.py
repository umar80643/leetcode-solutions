nums = [1,2,3,2]

d={}
for num in nums:
    if num in d:
        d[num]+=1
    else:
        d[num]=1


sum_val=0
for key,value in d.items():
    if value==1:
        sum_val+=key

print(sum_val)