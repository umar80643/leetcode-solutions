nums = [100, 4, 200, 1, 3, 2, 2, 5, 6, 7, 50, 51, 52, -1, 0, 1, 8]

s = set(nums)
print(s)

longest = 0
for num in s:
    if num-1 not in s:
        length = 1
        curr = num
        while curr+1 in s:
            length += 1
            curr += 1
        longest = max(length, longest)
print(longest)
