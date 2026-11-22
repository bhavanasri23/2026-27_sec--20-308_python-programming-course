# Unit-3 Task 36: Demonstrate lambda functions with map(), filter() and reduce()

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:", numbers)

# 1. Lambda Function - chinna anonymous function
square = lambda x: x * x
print("\n--- Lambda Function ---")
print("Square of 5 =", square(5))
print("Square of 8 =", square(8))

add = lambda a, b: a + b
print("Add 10 + 20 =", add(10, 20))

# 2. map() with lambda - prathi element ki operation apply chesthundi
print("\n--- map() with lambda ---")
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)

doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)

# 3. filter() with lambda - condition satisfy ayyevi matrame filter chesthundi
print("\n--- filter() with lambda ---")
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

odds = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers:", odds)

greater_than_5 = list(filter(lambda x: x > 5, numbers))
print("Greater than 5:", greater_than_5)

# 4. reduce() with lambda - anni values ni okate value ga marchuthundi
print("\n--- reduce() with lambda ---")
total = reduce(lambda a, b: a + b, numbers)
print("Sum of all numbers:", total)

product = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])
print("Product of 1 to 5:", product)

maximum = reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum:", maximum)