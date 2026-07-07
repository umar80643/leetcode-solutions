from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

groups = defaultdict(list)

for word in strs:
    count=[0]*26
    for ch in word:
        count[ord(ch)-ord('a')]+=1
    groups[tuple(count)].append(word)
print(list(groups.values()))

