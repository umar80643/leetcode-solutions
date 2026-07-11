height = [0,1,0,2,1,0,1,3,2,1,2,1]
n = len(height)
if n == 0:
    print(0)
leftMax =[0]*n
rightMax =[0]*n
leftMax[0] = height[0]
rightMax[n-1] = height[n-1]

for i in range(1,n):
    leftMax[i] = max(leftMax[i-1], height[i])

print(leftMax)

for i in range(n-2,-1,-1):
    rightMax[i] = max(rightMax[i+1], height[i])

water=[0]*n
max_unit=0
for i in range(len(height)):
   water[i] = min(leftMax[i], rightMax[i])- height[i]
   max_unit += water[i]
print(max_unit)