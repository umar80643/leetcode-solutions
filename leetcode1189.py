text = "leetcode"
arr =[0]*26
text1 ="balloon"
for i in range(len(text)):
    arr[ord(text[i])-97] += 1
print(arr)



print(min(arr[0],arr[1],arr[11]//2,arr[14]//2,arr[13]))






