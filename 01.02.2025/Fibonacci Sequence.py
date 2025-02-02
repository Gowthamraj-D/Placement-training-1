def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
num_terms = int(input("Enter the number of terms: "))
fib_sequence = fibonacci(num_terms)
print("Fibonacci sequence:", fib_sequence)
