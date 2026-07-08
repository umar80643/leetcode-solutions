import random
n=2
while n>0:
    x = random.randint(1,n)
    if 0<x<n and n%x==0:
        n=n-x


