s = "is2 sentence4 This1 a3"

s = list(s.split())


ans = [""] * len(s)

for i in range(len(s)):
    j = int(s[i][-1]) - 1
    ans[j] = s[i][:-1]

print(" ".join(ans))







