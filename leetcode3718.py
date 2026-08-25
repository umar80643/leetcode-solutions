nums = [8,2,3,4,6]
k = 2
s = set(nums)
i=1
while k:
    if k*i not in s:
        print(i*k)
        break
    else:
        i+=1


