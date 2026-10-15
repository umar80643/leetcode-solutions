num = 2
sum = 3

if sum > 9 * num:
    print("")


ans = "9"*(sum//9)

if sum % 9:
    ans += str(sum % 9)

print(ans + "0"*(num-len(ans)))

