n = 101
n = str(n)
l=[]
d={}
for num in n:
    l.append(int(num))
print(l)

for num in l:
    if num in d:
        d[num]+=1
    else:
        d[num]=1
print(d)
total=0
for key,value in d.items():
    total+=(key*value)
print(total)