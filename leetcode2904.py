s = "100011001"
k = 3

left=0
one=0
ans=""

for right in range(len(s)):
    if s[right]=="1":
        one+=1

    if one==k:

        while s[left]=="0":
            left+=1

        curr = s[left:right+1]

        if ans=="" or len(curr)<len(ans) or \
                (len(curr)==len(ans) and curr<ans):
            ans=curr


        left+=1
        one-=1


print(ans)




