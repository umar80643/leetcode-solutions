num = "1234"
sum_even=0
sum_odd=0
for i in range(0,len(num)):
    if i%2==0:
        sum_even+=int(num[i])
    else:
        sum_odd+=int(num[i])
if sum_even==sum_odd:
    print(True)
else:
    print(False)
