words = ["aba","aabb","abcd","bac","aabc"]

count = 0

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if set(words[i]) == set(words[j]):
            count += 1
print(count)

