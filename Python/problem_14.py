collatz_results = {}
collatz_results[1] = 1

def collatz_counter(n):
    if n in collatz_results:
        return collatz_results[n]
    elif n % 2 == 1:
        collatz_results[n] = 2 + collatz_counter((3 * n + 1)/2)
        return collatz_results[n]
    else:
        collatz_results[n] = 1 + collatz_counter(n/2)
        return collatz_results[n]


def main():
    max_so_far = 1
    for i in range(1,10**6):
        current = collatz_counter(i)
        if current > max_so_far:
            max_so_far = current
            best_start = i
    print(best_start)


if __name__ == "__main__":
    main()
