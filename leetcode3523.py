nums = [4,2,5,3,5]
stack = []
for num in nums:
    while stack and stack[-1] > num:
        num = max(num,stack.pop())
    stack.append(num)
print(stack)

