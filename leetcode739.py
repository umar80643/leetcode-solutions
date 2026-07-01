

temperatures = [73,74,75,71,69,72,76,73]
stack = []
ans =[0]*len(temperatures)

for i in range(len(temperatures)):
    while stack and temperatures[i] > temperatures[stack[-1]]:
         j = stack.pop()
         ans[j] = i - j
    stack.append(i)



print(ans)







