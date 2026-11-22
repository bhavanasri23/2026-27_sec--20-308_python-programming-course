from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() - square of each number using lambda
squared = list(map(lambda x: x**2, numbers))
print("Squared (map):", squared)

# filter() - even numbers using lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers (filter):", evens)

# reduce() - sum of all numbers using lambda
total = reduce(lambda x, y: x + y, numbers)
print("Sum (reduce):", total)
