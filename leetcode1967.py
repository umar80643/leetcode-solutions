patterns = ["a","abc","bc","d"]
word = "abc"
count = 0
for p in patterns:
    if p in word:
        count += 1
print(count)
