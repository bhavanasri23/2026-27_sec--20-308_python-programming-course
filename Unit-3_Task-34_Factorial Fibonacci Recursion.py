# Unit-3 Task 34: Find factorial and generate Fibonacci series using recursion

# 1. Factorial using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("--- Factorial using Recursion ---")
num = 5
print(f"Factorial of {num} =", factorial(num))
print(f"Factorial of 6 =", factorial(6))

# 2. Fibonacci using Recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("\n--- Fibonacci Series using Recursion ---")
n_terms = 10
print(f"Fibonacci series up to {n_terms} terms:")
for i in range(n_terms):
    print(fibonacci(i), end=" ")
print()

# Single term kuda chudochu
print("\nFibonacci term at position 7 =", fibonacci(7))