def factorial(n):
    prod = 1
    for i in range(2, n+1):
        prod *= i
    return prod

def sum_digits(k):
    digits = [int(char) for char in str(k)]
    return sum(digits)

def sum_digits_factorial(n):
    return sum_digits(factorial(n))

print(sum_digits_factorial(100))
