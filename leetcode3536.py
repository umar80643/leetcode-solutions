n=267
n=str(n)
l=[]
for num in n:
    l.append(int(num))
l.sort()

print(l[-1]*l[-2])
