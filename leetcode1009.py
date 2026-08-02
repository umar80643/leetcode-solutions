n= 10

n = str(bin(n)[2:])
complement = ''.join('1' if bit == '0' else '0' for bit in n)
print(int(complement , 2))