accounts = [[1,2,3],[3,2,1]]
best=0
for account in accounts:
    best = max(best ,sum(account))
print(best)