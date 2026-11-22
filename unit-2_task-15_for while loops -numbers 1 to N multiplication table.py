# Task 15: for and while loops

# 1. Print numbers from 1 to N using for loop
N = int(input("Enter N: "))
print("Numbers from 1 to N using for loop:")
for i in range(1, N + 1):
    print(i, end=" ")
print()

# 1. Print numbers from 1 to N using while loop
print("Numbers from 1 to N using while loop:")
i = 1
while i <= N:
    print(i, end=" ")
    i += 1
print()

# 2. Multiplication Table using for loop
num = int(input("Enter a number for table: "))
print("Table using for loop:")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 2. Multiplication Table using while loop
print("Table using while loop:")
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
