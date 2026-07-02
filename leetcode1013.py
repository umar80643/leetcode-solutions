arr = [0,2,1,-6,6,-7,9,1,2,0,1]

total_sum = sum(arr)
if total_sum % 3 != 0:
    print(False)

curr_total = 0
count = 0
part = total_sum // 3
for i in range(0, len(arr)):
    curr_total += arr[i]
    if curr_total == part:
        count += 1
        curr_total = 0
print(count >= 3)