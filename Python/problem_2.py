
#Supply n to compute F_n for n > 0
def fibonacci(n):
    f_n = 0                                #F_0
    f_n_minus_one = 1                      #F_-1
    for i in range(n):
        f_n_copy = f_n
        f_n += f_n_minus_one
        f_n_minus_one = f_n_copy
    return f_n

#Supply a bound upper_fib_bound to compute the sum of all even F_n such that F_n < upper_fib_bound
def sum_of_even_fib(upper_fib_bound):
    n = 3                                   #First even term is F_3
    sum = 0
    while fibonacci(n) <= upper_fib_bound:
        sum += fibonacci(n)
        n += 3                              # Every third term is even
    return sum

print(sum_of_even_fib(4000000))
