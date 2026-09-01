s = "abcde"
t = "edbac"
ans=0
for strs in s:
    ans+=abs(s.index(strs)-t.index(strs))
print(ans)