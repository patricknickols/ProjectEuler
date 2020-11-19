def fibonacci(n):
    answer = 2
    ultimate = 1
    for i in range(n):
        old_answer = answer
        answer += ultimate
        ultimate = old_answer
    return ultimate



def sum_of_even_fib(upper_fib_bound):
    n = 1
    sum = 0
    while fibonacci(n) <= upper_fib_bound:
        sum += fibonacci(n)
        n += 3
    return sum

answer = sum_of_even_fib(4000000)
print(fibonacci(1))
print(fibonacci(4))
print(fibonacci(7))
print(answer)
