"""module containing code for summing the
first 50 numbers of the fibonacci sequence 
"""


def sum_fibonacci(n):
    """ function for summing the
    first 50 fibonacci sequence
    num
    """

    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return sum(fib_sequence)

