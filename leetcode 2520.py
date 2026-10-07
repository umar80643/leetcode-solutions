num = 1248
n=num
count =0
while num:
    r=num%10
    if n%r==0:
        count +=1
    num //=10

print(count)

