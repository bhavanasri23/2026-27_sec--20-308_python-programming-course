# Task 12: Sum of first N Natural Numbers
# Algorithm:
# 1. START
# 2. Read N
# 3. Sum = N * (N + 1) // 2
# 4. Print Sum
# 5. STOP
# Flowchart: START -> Read N -> Sum = N(N+1)/2 -> Print Sum -> STOP

N = int(input("Enter N: "))

Sum = N * (N + 1) // 2

print("Sum of first", N, "natural numbers =", Sum)
