date = "2080-02-29"
s = date.split("-")
print(s)
ans=[]
for i in s:
    ans.append(bin(int(i))[2:])

strs = "-".join(ans)
print(strs)