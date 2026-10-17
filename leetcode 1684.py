from collections import Counter

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

ans =[]

for word in words:
    if Counter(allowed).keys() == Counter(word).keys():
        ans.append(word)

print(ans)


