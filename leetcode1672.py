accounts = [[1,2,3],[3,2,1]]
curr_sum = 0
for i in range(len(accounts)):
    best=0
    for j in range(len(accounts[0])):
        curr_sum += accounts[i][j]
    best = max(curr_sum, best)
print(best)