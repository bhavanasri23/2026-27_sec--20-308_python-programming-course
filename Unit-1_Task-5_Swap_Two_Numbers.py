# Swap two numbers without using a third variable

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("Before swapping: a =", a, ", b =", b)

# Swapping using arithmetic
a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, ", b =", b)
