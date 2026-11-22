# Demonstrate string formatting: format(), f-strings, % operator

name = "Bhavana"
age = 20
marks = 95.5678

# 1. Using format() method
print("1. Using format() method:")
print("My name is {} and I am {} years old.".format(name, age))
print("My name is {0} and I am {1} years old.".format(name, age))
print("Marks: {:.2f}".format(marks))

# 2. Using f-strings
print("\n2. Using f-strings:")
print(f"My name is {name} and I am {age} years old.")
print(f"Marks: {marks:.2f}")
print(f"Next year age will be {age + 1}")

# 3. Using % operator
print("\n3. Using % operator:")
print("My name is %s and I am %d years old." % (name, age))
print("Marks: %.2f" % marks)
