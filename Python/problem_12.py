import math

def primes(n):
    prime_list = [i for i in range(n+1)]
    for i in range(2,n):
        if prime_list[i] != 0:   #Check that i has not been crossed off
            for j in range(2*i,n+1,i): #Cross off every number i away
                prime_list[j] = 0
    prime_list[1] = 0
    return [prime for prime in prime_list if prime != 0]  #return list of uncrossed numbers

def prime_factors(big_num):
    factors = []
    for prime in primes(big_num // 2):  # cannot have a prime_factor larger than half of it, unless it is
        if big_num % prime == 0:
            factors.append(prime)
    return factors

def prime_factors_with_powers(n):
    primes_and_powers = {factor: 0 for factor in prime_factors(n)}
    for factor in primes_and_powers:
        counter = 0
        dividend = n
        while dividend % factor == 0:
            dividend = dividend / factor
            counter += 1
        primes_and_powers[factor] = counter
    return primes_and_powers

def triangular_number(n):
    return int((n*(n+1))/2)

def multiply_factor_dicts(x,y):
    result = {}
    for factor in x:
        if factor in y:
            result[factor] = x[factor] + y[factor]
        else:
            result[factor] = x[factor]
    for factor in y:
        if factor not in result:
            result[factor] = y[factor]
    return result

def count_factors_tri_number(n):
    first_factors = prime_factors_with_powers(n)
    second_factors = prime_factors_with_powers(n+1)
    result_factors = multiply_factor_dicts(first_factors, second_factors)
    result_factors[2] -= 1
    incr_exponents = [result_factors[key] + 1 for key in result_factors]
    return product(incr_exponents)

def product(list):
    result = 1
    for element in list:
        result *= element
    return result

def number_of_factors(n):
    factors_powers = prime_factors_with_powers(n)
    incr_exponents = [factors_powers[key] + 1 for key in factors_powers]
    return product(incr_exponents)

def first_tri_with_n_factors(n):
    counter = 3
    while count_factors_tri_number(counter) <= n:
        counter += 1
    return triangular_number(counter)

print(first_tri_with_n_factors(500))
