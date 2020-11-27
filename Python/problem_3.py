import math

def list_constructor(n):
    int_list = []
    for i in range(n):
        int_list.append(i)      #List is initialised with all values set to themselves
    return int_list

def primes(n):
    prime_list = list_constructor(n)
    for i in range(2,n):
        if prime_list[i] != 0:   #Check that i has not been crossed off
            for j in range(2*i,n,i): #Cross off every number i away
                prime_list[j] = 0
    prime_list[1] = 0
    return [prime for prime in prime_list if prime != 0]  #return list of uncrossed numbers


def prime_factorise(big_num):
    factors = []
    for prime in primes(big_num // 2):  # cannot have a prime_factor larger than half of it, unless it is
        if big_num % prime == 0:
            factors.append(prime)
    return factors

def is_prime(n):
    # Can check if it is in the list of primes less than or equal to itself but this is inefficient
    for prime in primes((round(math.sqrt(n)))+1):
        if n % prime == 0:
            return False
    else:
        return True


def largest_prime_factor(big_num):
    # Can compute last element of prime_factorise but this is inefficient for big numbers
    if is_prime(big_num):  # First test if it is prime
        return big_num
    else:
        for i in range(2,big_num):
            if big_num % i == 0 and is_prime(big_num // i):
                return (big_num // i)


print(largest_prime_factor(600851475143))
