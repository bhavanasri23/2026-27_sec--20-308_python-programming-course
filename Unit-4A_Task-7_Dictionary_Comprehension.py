# Dictionary of numbers and their squares using dictionary comprehension
squares = {x: x**2 for x in range(1, 11)}

print("Numbers and their Squares:")
print(squares)

for num, square in squares.items():
    print(num, ":", square)
