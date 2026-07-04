nums = [3,2,3]
candidate1 = None
candidate2 = None
count1 = 0
count2 = 0
for num in nums:
    if num == candidate1:
        count1 += 1
    elif num == candidate2:
        count2 += 1
    elif count1 == 0:
        candidate1 = num
        count1 = 1
    elif count2 == 0:
        candidate2 = num
        count2 = 1
    else:
        count1 -= 1
        count2 -= 1
count1 =0
count2 =0
for num in nums:
    if num == candidate1:
        count1 += 1
    elif num == candidate2:
        count2 += 1
ans =[]
if count1 > len(nums)//3:
    ans.append(candidate1)
if count2 > len(nums)//3:
    ans.append(candidate2)
print(ans)
