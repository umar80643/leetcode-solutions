n=4
sum_odd = n**2
sum_even = n*(n+1)



while sum_odd != sum_even:
    if sum_odd > sum_even:
        sum_odd = sum_odd - sum_even
    else:
        sum_even = sum_even - sum_odd
print(sum_odd)