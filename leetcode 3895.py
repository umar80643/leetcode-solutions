nums = [12, 54, 32, 22]

digit = 2
count=0
for num in nums:
    while num>0:
        r = num%10
        if r==digit:
            count+=1
        num //= 10
print(count)
