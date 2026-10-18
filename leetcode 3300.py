nums = [18,43,34,16]
l=[]

for num in nums:
    ans=0
    while num:
        r = num % 10
        ans += r
        num //= 10
    l.append(ans)
print(l)

