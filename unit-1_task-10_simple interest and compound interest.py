# Task 10: Simple Interest and Compound Interest

P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (in years): "))

# Simple Interest
SI = (P * R * T) / 100
print("Simple Interest =", SI)

# Compound Interest
CI = P * (1 + R/100) ** T - P
print("Compound Interest =", CI)
print("Total Amount =", P + CI)
