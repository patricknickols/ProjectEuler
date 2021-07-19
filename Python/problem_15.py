def product(list):
    result = 1
    for element in list:
        result *= element
    return result

def factorial(n):
    return product(range(1,n+1))

def n_choose_k(n,k):
    return factorial(n) / (factorial(n-k) * factorial(k))


print(n_choose_k(40,20))
