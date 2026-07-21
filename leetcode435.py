intervals = [[1,2],[2,3]]

intervals.sort()
lastinterval = intervals[0]

count = 0
for start , end in intervals[1:]:
    if start < lastinterval[-1]:
        count += 1
        if end < lastinterval[-1]:
            lastinterval = [start,end]
    else:
        lastinterval = [start,end]





print(count)