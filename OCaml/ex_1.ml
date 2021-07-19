let rec count_multiples_of_x_below_y x y =
    if y <= x then 0
    else 1 + count_multiples_of_x_below_y x (y-x);;

let sum_multiples_of_x_below_y x y =
     ((x + ((count_multiples_of_x_below_y x y) * x)) * (count_multiples_of_x_below_y x y)) / 2;;
    
let answer = (sum_multiples_of_x_below_y 3 1000) + (sum_multiples_of_x_below_y 5 1000) - (sum_multiples_of_x_below_y 15 1000);;

print_int(answer);;
