word = "xycdefghij"
n = len(word)
ans=0
for i in range(n):
    ans +=(i//8)+1
    print(ans)
print(ans)