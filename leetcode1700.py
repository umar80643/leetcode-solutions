students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
d={}
res = len(students)
for s in students:
    if s in d:
        d[s]+=1
    else:
        d[s]=1

print(d)

for food in sandwiches:
    if d[food]>0:
        res-=1
        d[food]-=1
    else:
        print(res)

print(d,res)


#or


d = {}
res = len(students)

for s in students:
    d[s] = d.get(s, 0) + 1

for food in sandwiches:
    if d.get(food, 0) > 0:
        res -= 1
        d[food] -= 1
    else:
        print(res)

print(res)