# Task 16: sum, count, reverse of digits

num = int(input("Enter a number: "))
temp = num
sum_digits = 0
count = 0
reverse = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    reverse = reverse * 10 + digit
    count += 1
    temp //= 10

print("Sum of digits:", sum_digits)
print("Count of digits:", count)
print("Reverse of number:", reverse)
