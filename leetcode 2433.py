pref = [5,2,0,3,1]

ans =[pref[0]]

for i in range(1,len(pref)):
    ans.append(pref[i]^pref[i-1])
print(ans)



