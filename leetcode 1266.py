points = [[1,1],[3,4],[-1,0]]
prev_start = points[0][0]
prev_end = points[0][-1]


total_time = 0

for start, end in points[1:]:
    sum_start = abs(prev_start - start)
    sum_end = abs(prev_end - end)
    total_time += max(sum_end , sum_start)
    prev_start = start
    prev_end = end


print(total_time)




