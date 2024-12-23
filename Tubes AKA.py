import time

# Fungsi Fibonacci Iteratif
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# Fungsi Fibonacci Rekursif
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Fungsi untuk membandingkan performa
def compare_fibonacci_methods_for_range(n_values):
    print(f"{'n':<5} {'Iterative Result':<20} {'Iterative Time (s)':<20} {'Recursive Result':<20} {'Recursive Time (s)':<20}")
    print("-" * 90)
    
    for n in n_values:
        # Iterative
        start_time = time.time()
        fib_iterative = fibonacci_iterative(n)
        iterative_time = time.time() - start_time
        
        # Recursive
        start_time = time.time()
        try:
            fib_recursive = fibonacci_recursive(n)
            recursive_time = time.time() - start_time
        except RecursionError:
            fib_recursive = "Recursion Limit Exceeded"
            recursive_time = "N/A"
        
        # Print results
        print(f"{n:<5} {fib_iterative:<20} {iterative_time:<20.10f} {fib_recursive:<20} {recursive_time:<20}")


# Jalankan perbandingan
if __name__ == "__main__":
    n_values = [5, 10, 15, 20, 25, 30, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]  
    compare_fibonacci_methods_for_range(n_values)
