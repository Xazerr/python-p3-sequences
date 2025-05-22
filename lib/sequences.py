def print_fibonacci(n):
    if n <= 0:
        print([])  # empty list for non-positive input
        return

    fib = [0, 1]

    # If n == 1, print just [0]
    if n == 1:
        print([0])
        return

    while len(fib) < n:
        # Next number is sum of last two numbers
        next_value = fib[-1] + fib[-2]
        fib.append(next_value)

    print(fib)
