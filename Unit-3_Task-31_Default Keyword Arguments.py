# Unit-3 Task 31: Demonstrate default and keyword arguments

# 1. Default Arguments
# name ki default value "Guest" icham, ivvakapoyina error raadu
def greet(name="Guest", city="Vijayawada"):
    print(f"Hello {name} from {city}")

print("--- Default Arguments ---")
greet()  # rendu default values use avthayi
greet("Bhavana")  # city default
greet("Bhavana", "Hyderabad")

# 2. Keyword Arguments
# order marchina kuda name tho pilusthe correct ga velthundi
def student_info(name, age, course):
    print(f"Name: {name}, Age: {age}, Course: {course}")

print("\n--- Keyword Arguments ---")
student_info(age=20, course="B.Tech", name="Bhavana")
student_info(name="Siri", age=19, course="CSE")

# 3. Default + Keyword kalipi
def calculate_area(length=10, breadth=5):
    return length * breadth

print("\n--- Default + Keyword ---")
print("Default Area:", calculate_area())
print("Area (length=4):", calculate_area(length=4))
print("Area (breadth=8, length=6):", calculate_area(breadth=8, length=6))