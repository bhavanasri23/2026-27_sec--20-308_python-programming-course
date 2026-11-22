# Task 17: Palindrome and Armstrong

num = int(input("Enter a number: "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

# 1. Palindrome Check
if num == reverse:
    print(num, "is a Palindrome")
else:
    print(num, "is NOT a Palindrome")

# 2. Armstrong Check
temp = num
n = len(str(num))
arm_sum = 0

while temp > 0:
    digit = temp % 10
    arm_sum += digit ** n
    temp //= 10

if num == arm_sum:
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")
