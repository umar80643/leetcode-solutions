matrix = [[0,1,1],[1,0,1],[1,1,0]]

ans=[]
for i in matrix:
    ans.append(i.count(1))
print(ans)