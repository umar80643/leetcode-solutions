s="hello"
ans =0
for i in range (1,len(s)):
    ans+=abs(ord(s[i])-ord(s[i-1]))
print(ans)
