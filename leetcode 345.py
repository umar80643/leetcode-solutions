s="IceCreAm"


l=0
r=len(s)-1

s=list(s)

while l<r:
    if s[l] in "AEIOUaeiou" and s[r] in "AEIOUaeiou":
        s[l] , s[r] = s[r] , s[l]
        l+=1
        r-=1
    elif s[l] not in "AEIOUaeiou":
        l+=1
    elif s[r] not in "AEIOUaeiou":
        r-=1
    else:
        l+=1
        r-=1

print("".join(s))
