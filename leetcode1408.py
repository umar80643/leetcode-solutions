words=["mass","as","hero","superhero"]
l=[]
for i in range(len(words)):
    for j in range(i+1,len(words)):
        if words[j] in words[i]:
            if words[j] not in l:
                l.append(words[j])
                j+=1
            else:
                j+=1
        elif words[i] in words[j]:
            if words[i] not in l:
                l.append(words[i])
                j+=1
            else:
                j+=1
        else:
            j+=1
print(l)
