# Task 18: Factorial and Fibonacci

# 1. Factorial of a number
num = int(input("Enter a number for factorial: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial of", num, "is:", fact)

# 2. Fibonacci series up to N terms
N = int(input("Enter N for Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(N):
    print(a, end=" ")
    a, b = b, a + b