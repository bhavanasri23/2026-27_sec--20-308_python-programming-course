# Task 19: Prime Numbers

# 1. Check whether a number is Prime or Not
num = int(input("Enter a number: "))
if num < 2:
    print(num, "is NOT a Prime Number")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a Prime Number")
    else:
        print(num, "is NOT a Prime Number")

# 2. Print all primes between 1 and N
N = int(input("Enter N: "))
print("Prime numbers between 1 and", N, ":")
for n in range(2, N + 1):
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")
