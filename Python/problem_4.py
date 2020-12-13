def is_palindrome(number):
	return (str(number) == str(number)[::-1])

def largest_palindrome_product_n_digits(n):
	largest = 0
	for i in range(10**(n-1), 10**(n)):
		for j in range(10**(n-1), 10**(n)):
			product = i * j
			if is_palindrome(product) and product > largest:
				largest = product
	return largest


print(largest_palindrome_product_n_digits(3))
