

title = "First leTTeR of EACH Word"

l=title.split()

ans=[]
for s in l:
    if len(s)>2:
        s=s.lower()
        s=s.title()
        ans.append(s)
    else:
        s=s.lower()
        ans.append(s)

print(" ".join(ans))

