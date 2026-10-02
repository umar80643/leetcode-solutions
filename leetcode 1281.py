
n = 234
mutiply_val =1
sum_val =0
while n>0:
    r = n%10
    sum_val+=r
    mutiply_val*=r
    n//=10

print(sum_val)
print(mutiply_val)
print(mutiply_val - sum_val)