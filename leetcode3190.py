nums = [1,2,3,4]
count = 0
for num in nums:
    if num % 3==0:
        pass
    elif not num % 3==0:
        num = num + 1
        count +=1
    else:
        num = num - 1
        count +=1

print(count)