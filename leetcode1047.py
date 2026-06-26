s ="abbaca"
stack = []
for i in range(0,len(s)):
    if stack and s[i]==stack[-1]:
        stack.pop()
    else:
        stack.append(s[i])
print(stack)
