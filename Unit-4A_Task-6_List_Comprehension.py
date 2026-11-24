# Squares of 1 to 10 using list comprehension
squares = [x**2 for x in range(1, 11)]
print("Squares of 1 to 10:", squares)

# Even numbers using list comprehension
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers from 1 to 10:", even_numbers)
