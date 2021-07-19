def factorial(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod

def sum_digits(k):
    sum = 0
    for char in str(k):
        sum += int(char)
    return sum

def sum_digits_factorial(n):
    return sum_digits(factorial(n))

print(sum_digits_factorial(100))
