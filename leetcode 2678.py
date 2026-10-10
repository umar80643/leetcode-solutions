details = ["1313579440F2036","2921522980M5644"]

count=0
for detail in details:
    if int(detail[11:13]) > 60:
        count+=1

print(count)