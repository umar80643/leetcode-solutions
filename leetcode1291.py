low = 100
high = 300
s="123456789"
ans=[]

for length in range(len(str(low)),len(str(high))+1):
    for start in range(10-length):
        nums =int(s[start:start+length])
        if low <= nums <= high:
            ans.append(nums)
print(ans)

