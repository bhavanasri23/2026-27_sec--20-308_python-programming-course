# Unit-2 Task 23: String Creation, Operations, Methods and Formatting

# 1. String Creation
s1 = "Hello"
s2 = 'Python'
print("s1:", s1)
print("s2:", s2)

# 2. Operations
print("\n--- Operations ---")
print("Concatenation:", s1 + " " + s2)
print("Repetition:", s1 * 3)
print("Slicing [0:5]:", "Hello Python"[0:5])
print("Slicing [6:]:", "Hello Python"[6:])
print("Slicing [::-1] Reverse:", "Hello Python"[::-1])

# 3. Methods
print("\n--- Methods ---")
text = "  Hello, Python World  "
print("Original:", text)
print("upper():", text.upper())
print("lower():", text.lower())
print("strip():", text.strip())
print("split():", text.strip().split())
print("join():", "-".join(["Hello", "Python"]))
print("replace():", text.replace("Python", "Bhavana"))
print("find() Python:", text.find("Python"))

# 4. Formatting
print("\n--- Formatting ---")
name = "Bhavana"
age = 20
print("format(): My name is {} and I am {} years old.".format(name, age))
print(f"f-string: My name is {name} and I am {age} years old.")
print(" % operator: My name is %s and I am %d years old." % (name, age))