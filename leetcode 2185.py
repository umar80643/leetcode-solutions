words = ["pay","attention","practice","attend"]
pref = "at"
k = len(pref)
count = 0
for word in words:
    if pref in word[:k]:
        count +=1
print(count)