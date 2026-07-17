
flowerbed = [1,0,0,0,1]
n = 2
count = 0
for i in range(len(flowerbed)):
    left_empty = (i == 0 or flowerbed[i - 1] == 0)
    right_empty = (i == len(flowerbed)-1 or flowerbed[i+1] == 0)
    if flowerbed[i] == 0 and left_empty and right_empty:
        flowerbed[i] = 1
        count+=1
print(count==n)