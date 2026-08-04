nums = [7,8,6,9]
max_val = max(nums)
min_val = min(nums)
l =[]
for i in range(min_val, max_val+1):
    if i not in nums:
        l.append(i)
print(l)
