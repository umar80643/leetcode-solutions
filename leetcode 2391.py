garbage = ["G","P","GP","GG"]
travel = [2,4,3]

total = 0

last = {'G':0, 'p':0 , 'M':0}


for i , house  in  enumerate(garbage):
    total += len(house)

    for g in house:
        last[g] =i

for i in range(1,len(travel)):
    travel[i]+= travel[i-1]

for g in last:
    if last[g] > 0:
        total+= travel[last[g]-1]

print(total)

