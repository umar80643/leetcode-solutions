words = ["abcd","def","xyz"]
weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]


l=[]
for word in words:
    ans=0
    i=0
    while i<len(word):
        pos = ord(word[i])-ord('a')
        ans +=weights[pos]
        i+=1
    l.append(ans)
print(l)
strs=[]
for i in l:
    print(i)
    num = chr((25-(i%26))+97)
    strs.append(num)
print("".join(strs))






