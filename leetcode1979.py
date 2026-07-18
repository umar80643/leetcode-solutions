nums = [2, 5, 6, 9, 10]
x = min(nums)
y = max(nums)
while x != y:
    if x > y:
        x = x - y
    if y > x:
        y = y - x
print(x)
