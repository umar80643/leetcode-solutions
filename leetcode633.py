from math import floor, sqrt

c = 4
l=0
r=floor(sqrt(c))
while l<=r:
    total = l**2 + r**2
    if total == c:
        print(True)
        break
    if total < c:
        l+=1
    else:
        r-=1
print(False)
