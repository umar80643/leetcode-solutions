s = "(1+(2*3)+((8)/4))+1"
count=0
max_count = 0
for i in s:
    if i == "(":
        count+=1
    elif i == ")":
        count-=1
    max_count = max(max_count, count)


print(max_count)
