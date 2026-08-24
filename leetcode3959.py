n = 19
digitSum = 0
squareSum = 0
while n > 0:
    r=n%10
    digitSum+=r
    squareSum+=r*r
    n=n//10
print(digitSum)
print(squareSum)
print(abs(digitSum-squareSum)>=50)
