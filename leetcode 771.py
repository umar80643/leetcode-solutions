jewels = "aA"
stones = "aAAbbbb"

count = 0
for char in jewels:
    count += stones.count(char)

print(count)
