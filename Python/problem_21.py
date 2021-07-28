from itertools import combinations
from math import prod

def is_amicable(n):
    if n in primes(n+1):
        return False
    sum_of_divisors = sum_divisors(n)
    other_sum = sum_divisors(sum_of_divisors)
    return other_sum == n and n != sum_of_divisors

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

def sum_divisors(n):
    factors = prime_factors_with_powers(n)
    factor_list = [factor for factor in factors for i in range(factors[factor])]
    all_factors = {1}
    for i in range(1, len(factor_list)):
        for comb in combinations(factor_list, i):
            all_factors.add(prod(comb))
    return sum(all_factors)



def main():
    sum_so_far = 0
    for i in range(2,10000):
        if is_amicable(i):
            sum_so_far += i
    print(sum_so_far)

if __name__ == "__main__":
    main()
