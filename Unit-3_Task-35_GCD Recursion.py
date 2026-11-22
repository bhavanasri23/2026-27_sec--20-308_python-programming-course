# Unit-3 Task 35: Find GCD of two numbers using recursion

# Euclidean Algorithm tho recursion
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print("--- GCD using Recursion ---")
a = 48
b = 36
print(f"GCD of {a} and {b} =", gcd(a, b))

print(f"GCD of 12 and 18 =", gcd(12, 18))
print(f"GCD of 100 and 25 =", gcd(100, 25))

# User input tho kuda try cheyochu
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(f"GCD of {a} and {b} =", gcd(a, b))