def fib(n):
    f_n = 0
    f_n_minus_one = 1
    for i in range(n):
        f_n_copy = f_n
        f_n += f_n_minus_one
        f_n_minus_one = f_n_copy
    return f_n

def is_even(n):
    return n % 2 == 0

def fib_generator(up_bound):
    index = 1
    while fib(index) < up_bound:
        yield(fib(index))
        index += 1

def sum_of_even_fib(up_bound): # This function is slower (by a constant factor ~3) than it could be since it calculates unnecessary (odd) terms, see old implementation for a less readable, but faster alternative
    even_fibs = [x for x in fib_generator(up_bound) if is_even(x)]
    return sum(even_fibs)

print(sum_of_even_fib(4000000))
