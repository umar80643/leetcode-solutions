tickets = [5,1,1,1]
k = 0
res =0
for i , ticket in enumerate(tickets):
    if i<=k:
        res += min(ticket,tickets[k])
    else:
        res += min(ticket,tickets[k]-1)
print(res)



