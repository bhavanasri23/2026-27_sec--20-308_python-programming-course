# Unit-4B Task-2: Multiple Except Blocks

fruits = ["apple", "banana", "mango", "orange", "grapes"]

try:
    index = int(input("Enter index (0-4): "))
    print("Selected fruit:", fruits[index])

except ValueError:
    print("Error: Please enter a valid integer!")

except IndexError:
    print("Error: Index out of range! Enter 0 to 4 only.")

print("Program finished")
