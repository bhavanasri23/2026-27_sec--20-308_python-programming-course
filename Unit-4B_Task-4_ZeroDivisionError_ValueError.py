# Unit-4B Task-4: ZeroDivisionError and ValueError

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print("Result:", result)

except ValueError:
    print("Error: Please enter valid integers only!")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
