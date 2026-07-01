prices = [8,4,6,2,3]
stack = []
ans = prices

for i in range(len(prices)):
    while stack and prices[stack[-1]] >= prices[i]:
        idx = stack.pop()
        ans[idx] = prices[idx] - prices[i]

    stack.append(i)

print(ans)
