nums = [8,1,2,2,3]

temp = sorted(nums)

print(temp)
d = {}
for i, v in enumerate(temp):
    if v not in d:
        d[v] = i
res = []
for i in nums:
    res.append(d[i])

print(res)