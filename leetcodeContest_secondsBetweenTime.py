startTime = "12:34:56"
endTime = "13:00:00"

h1, m1, s1 = map(int, startTime.split(":"))
h2, m2, s2 = map(int, endTime.split(":"))
start = h1 * 3600 + m1 * 60 + s1
end = h2 * 3600 + m2 * 60 + s2
print(end - start)
