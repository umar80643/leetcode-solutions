nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
d={}
for num in nums:
    d[num]=d.get(num,0)+1
print(d)


