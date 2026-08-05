n = 10
m = 3
num1=0
num2=0
for i in range(n+1):
    if i%m==0:
        num1+=i
    else:
        num2+=i
print(num2-num1)