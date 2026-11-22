# Demonstrate type conversion (int, float, string)

# int to float and string
a = 10
print("a =", a, "type:", type(a))
print("int to float:", float(a), "type:", type(float(a)))
print("int to string:", str(a), "type:", type(str(a)))

# float to int and string
b = 12.75
print("\nb =", b, "type:", type(b))
print("float to int:", int(b), "type:", type(int(b)))
print("float to string:", str(b), "type:", type(str(b)))

# string to int and float
c = "25"
print("\nc =", c, "type:", type(c))
print("string to int:", int(c), "type:", type(int(c)))
print("string to float:", float(c), "type:", type(float(c)))

# User input (by default string) conversion
num_str = input("\nEnter a number: ")
print("Input type:", type(num_str))
num_int = int(num_str)
num_float = float(num_str)
print("Converted to int:", num_int, "type:", type(num_int))
print("Converted to float:", num_float, "type:", type(num_float))
print("int + 10 =", num_int + 10)
