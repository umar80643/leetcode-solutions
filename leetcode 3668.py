order = [3,1,2,5,4]
friends = [1,3,4]
l=[]
for num in order:
    if num in friends:
        l.append(num)
print(l)