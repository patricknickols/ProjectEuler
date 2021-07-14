def primes(n):
    prime_list = [i for i in range(n)]
    for i in range(2,n):
        if prime_list[i] != 0:   #Check that i has not been crossed off
            for j in range(2*i,n,i): #Cross off every number i away
                prime_list[j] = 0
    prime_list[1] = 0
    return [prime for prime in prime_list if prime != 0]  #return list of uncrossed numbers

def sum_primes(n):
    prime_list = primes(n)
    return sum(prime_list)

print(sum_primes(2000000))
