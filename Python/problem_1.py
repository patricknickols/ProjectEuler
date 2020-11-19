def sum_multiples_of_x(x, upper_bound):
    sum = 0
    i = 0
    while i < upper_bound:
        sum += i
        i += x
    return sum

total_3s_under_1000 = sum_multiples_of_x(3,1000)
total_5s_under_1000 = sum_multiples_of_x(5,1000)
total_15s_under_1000 = sum_multiples_of_x(15,1000)

answer = total_3s_under_1000 + total_5s_under_1000 - total_15s_under_1000

print(answer)
