num1 = 198
num2 = 202
waviness = 0

for i in range(num1, num2 + 1):
    digits = [int(x) for x in str(i)]

    for j in range(1, len(digits) - 1):
        if (digits[j - 1] > digits[j] < digits[j + 1]) or \
           (digits[j - 1] < digits[j] > digits[j + 1]):
            waviness += 1

print(waviness)
