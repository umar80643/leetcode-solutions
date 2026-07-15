num = 16
if num<2:
    print(True)
left = 2
right = num//2

while left<=right:
    mid = (left+right)//2
    sq = mid*mid
    if sq == num:
        print(True)
        break
    elif sq < num:
        left = mid+1
    else:
        right = mid-1
print(False)