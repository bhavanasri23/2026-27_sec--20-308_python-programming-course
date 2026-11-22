# Task 14: nested if, elif ladder

# 1. Largest and Smallest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c

if a < b:
    if a < c:
        smallest = a
    else:
        smallest = c
else:
    if b < c:
        smallest = b
    else:
        smallest = c

print("Largest:", largest)
print("Smallest:", smallest)

# 2. Assign a Grade (elif ladder)
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
elif marks >= 40:
    print("Grade: E")
else:
    print("Grade: F - Fail")

# 3. Check Triangle is Valid or Not
a1 = int(input("Enter angle 1: "))
a2 = int(input("Enter angle 2: "))
a3 = int(input("Enter angle 3: "))
if a1 + a2 + a3 == 180 and a1 > 0 and a2 > 0 and a3 > 0:
    print("Triangle is Valid")
else:
    print("Triangle is NOT Valid")