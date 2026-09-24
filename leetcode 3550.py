nums = [1,10,11]
i=0
for num in nums:
    total=0
    while num>0:
        r=num%10
        total+=r
        num//=10
    if total==i:
        print(i)
        break
    i+=1

