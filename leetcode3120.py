word = "aaAbcBC"
lower = set()
upper = set()

for ch in word:
    if ch.islower():
        lower.add(ch)
    else:
        upper.add(ch)
ans=0
for ch in lower:
    if ch.upper() in upper:
        ans += 1
print(ans)


