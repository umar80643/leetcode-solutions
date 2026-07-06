haystack = "sadbutsad"
needle = "sad"

m = len(needle)
n = len(haystack)

if m ==0:
    print(0)
for i in range(n-m+1):
    j =0
    while j<m and haystack[i+j] ==needle[j]:
        j +=1
    if j==m:
        print(i)
print(-1)