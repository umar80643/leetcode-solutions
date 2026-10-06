s = "()))(("

open =0
ans =0

for i in s:
    if i == "(":
        open +=1
    else:
        if open>0:
            open -= 1
        else:
            ans +=1

ans += open
print(ans)






