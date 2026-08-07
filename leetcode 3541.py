s = "successes"
d={}
for i in  s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

vowels = "aeiou"
max_vowels = 0
max_consonant=0
for key,value in d.items():
    if key in vowels:
        max_vowels = max(max_vowels,value)
    else:
        max_consonant = max(max_consonant,value)

print(max_vowels,max_consonant)
print(max_vowels+max_consonant)




