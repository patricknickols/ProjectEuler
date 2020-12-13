def largest_power_less_than(base, upper_bound):
    largest_power = 0
    i = 1
    test = base
    while test < upper_bound:
        test = base ** i
        largest_power = i-1
        i += 1
    return largest_power

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


def largest_evenly_divisible(n):
    primes_and_powers = {}
    for prime in primes(n):
        primes_and_powers[prime] = largest_power_less_than(prime, n)
    product = 1
    for prime in primes_and_powers:
        product *= (prime ** primes_and_powers[prime])
    return product

print(largest_evenly_divisible(20))
