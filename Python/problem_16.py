big_num = 2**1000
digits = [digit for digit in str(big_num)]
for i in range(len(digits)):
    digits[i] = int(digits[i])

print(sum(digits))
