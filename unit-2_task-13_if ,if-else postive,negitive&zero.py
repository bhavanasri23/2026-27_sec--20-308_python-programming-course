# Task 13: if, if-else

# 1. Positive, Negative or Zero
num = int(input("Enter a number: "))
if num > 0:
    print(num, "is Positive")
elif num < 0:
    print(num, "is Negative")
else:
    print(num, "is Zero")

# 2. Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")

# 3. Eligible to Vote
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to Vote")
else:
    print("NOT Eligible to Vote")
