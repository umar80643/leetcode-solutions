x = 18
original = x
total = 0
while x:
    r = x % 10
    total += r
    x //= 10

if original % total == 0:
    print(total)

