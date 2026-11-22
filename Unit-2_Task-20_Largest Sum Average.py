# Unit-2 Task 20: Read N numbers and find largest, sum and average

N = int(input("Enter how many numbers (N): "))

total = 0
largest = 0

for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    total += num
    if i == 0 or num > largest:
        largest = num

average = total / N

print("Largest number:", largest)
print("Sum:", total)
print("Average:", average)