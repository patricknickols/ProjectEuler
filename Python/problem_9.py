import math

#Checks if a float is approximately an int
def is_int(k):
    return k - (k//1) <= 0.00001

#Checks if these two numbers form a pythagorean pythagorean triple, a^2 + b^2 = c^2 for integer c
def pythag_triple(a,b):
    c = math.sqrt(a**2 + b**2)
    return is_int(c)

for i in range(1,700): # Some basic inequalities can demonstrate that a and b must be less than 1000 sqrt(2)/2 ~ 700
    for j in range(1,700):
        if pythag_triple(i,j) and (abs(i + j + math.sqrt(i**2 + j**2) - 1000) <= 0.00001):
            print(i * j * math.sqrt(i**2 + j**2))
