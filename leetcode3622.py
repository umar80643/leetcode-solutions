n=23
original_val = n
total=0
product=1
while n>0:
    r=n%10
    total=total+r
    product=product*r
    n=n//10

if original_val % (product+total)==0:
    print("True")
else:
    print("False")