let rec fibonacci n =
   if n < 2 && n >= 0 then 1
   else fibonacci (n-1) + fibonacci (n-2);;

let is_even n = n mod 2 = 0;;

let rec sum_even_fib n upper_bound =
    if fibonacci n > upper_bound then 0
    else
        if is_even (fibonacci n) then 
            fibonacci n + sum_even_fib (n+1) upper_bound
        else sum_even_fib (n+1) upper_bound;;

print_int(sum_even_fib 1 4000000);;
