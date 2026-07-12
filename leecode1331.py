arr = [37,12,28,9,100,56,80,5,12]
l= arr.copy()


arr.sort()

rank =1
d={}
for i in range(len(arr)):
    if  arr[i] not in d:
        d[arr[i]] = rank
        rank +=1


print(d)
ans =[]


for position  in l:
    ans.append(d[position])
print(ans)