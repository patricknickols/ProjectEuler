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


def triangular_number(n):
    return (n * (n+1))/2

def prime_factorise_with_powers(n):
    primes_and_powers = []
    for prime in primes(n):
        primes_and_powers[prime] = largest_power_less_than(prime, n)
    return primes_and_powers
