def find_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum of (10, 20, 30):", find_sum(10, 20, 30))
print("Sum of (5, 15):", find_sum(5, 15))
print("Sum of (1, 2, 3, 4, 5):", find_sum(1, 2, 3, 4, 5))
print("Sum of (100):", find_sum(100))
