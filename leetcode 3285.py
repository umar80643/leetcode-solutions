height = [1,2,3,4,5]
threshold = 2
ans=[]
for i in range(1,len(height)):
    if height[i-1] > threshold:
        ans.append(i)
print(ans)