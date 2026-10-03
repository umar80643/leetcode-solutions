num = 526

reverse1 = int(str(num)[::-1])
reverse2 = int(str(reverse1)[::-1])

if num == reverse2:
    print("True")
