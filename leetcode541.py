s = "abcdefg"
k = 2
s=list(s)
for i in range(0,len(s),2*k):
    s[i:i+k]=reversed(s[i:i+k])

print("".join(s))
