word = "abcdefd"
ch = "d"

for i in range(len(word)):
    if word[i] == ch:
        word = word[:i+1][::-1] + word[i+1:]
        break
print(word)