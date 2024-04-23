# Generate Fibonacci series up to n terms

def generate_fibonacci(n):
    fibonacci_series = [0, 1]  # Initialize the series with the first two terms
    for i in range(2, n):
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)
    return fibonacci_series

# Example usage:
num_terms = int(input("Enter the number of terms: "))
fibonacci_sequence = generate_fibonacci(num_terms)
print("Fibonacci series up to", num_terms, "terms:", fibonacci_sequence)
