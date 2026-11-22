# Unit-3 Task 30: Define and call a function with parameters and return values

# 1. Function with parameters and return value
def add(a, b):
    return a + b

# 2. Function with parameters and return value
def subtract(a, b):
    return a - b

# 3. Function with parameters and return value
def multiply(a, b):
    return a * b

# 4. Function to find largest of two numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b

# Calling the functions
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Largest:", largest(10, 5))

# Function with single parameter and return
def square(n):
    return n * n

print("\nSquare of 6:", square(6))

# Function with no return - just prints
def greet(name):
    print("\nHello,", name)

greet("Bhavana")