n =1004590
ans=0

for k in range(1,6):
    start = 10**(3*k)


    if n>=start:
        ans += (n-start+1)



print(ans)





