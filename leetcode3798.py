s = "221"

l = 0
r = len(s)

while l < r:
    print(s[l:r])
    if int(s[l:r]) % 2 == 0:
        print(s[l:r])
        break
    else:
        r=r-1
print("")