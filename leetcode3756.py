s = "10203004"


queries = [[0,7],[1,3],[4,6]]
l=[]

for start, end in queries:
    total = s[start:end+1]
    i=0
    num=""
    sum1=0
    while i<len(total):
        if total[i]!="0":
            sum1+=int(total[i])
            num+=total[i]
            i+=1
    l.append(sum1*int(num))

print(l)