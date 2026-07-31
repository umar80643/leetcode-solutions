word = "abzaqsqcyrbzsrvamylmyxdjl"
d={}
for s in word:
    if s in d:
        d[s]+=1
    else:
        d[s]=1
res =0
word = sorted(d, key=d.get, reverse=True)
for i in range(len(word)):
    res += ((i//8)+1)*d[word[i]]
print(res)