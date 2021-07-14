import math

def primes(n):
    prime_list = [i for i in range(n+1)]
    for i in range(2,n):
        if prime_list[i] != 0:   #Check that i has not been crossed off
            for j in range(2*i,n+1,i): #Cross off every number i away
                prime_list[j] = 0
    prime_list[1] = 0
    return [prime for prime in prime_list if prime != 0]  #return list of uncrossed numbers

def triangular_number(n):
    return int((n*(n+1))/2)

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
    counter = 1200
    while number_of_factors(triangular_number(counter)) <= n:
        counter += 1
    print(counter)
    return triangular_number(counter)

print(first_tri_with_n_factors(500))
