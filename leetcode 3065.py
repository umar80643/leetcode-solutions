nums = [2, 11, 10, 1, 3]
k = 10

print(sum(1 for num in nums if not num >= k))