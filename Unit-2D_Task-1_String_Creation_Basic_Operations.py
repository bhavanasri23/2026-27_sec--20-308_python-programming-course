# String creation and basic operations (concatenation, repetition, slicing)

# String creation
str1 = "Hello"
str2 = 'Python'
str3 = """Welcome to Python Programming"""
print("String 1:", str1)
print("String 2:", str2)
print("String 3:", str3)

# Concatenation
result = str1 + " " + str2
print("\nConcatenation:", result)

# Repetition
print("Repetition:", str1 * 3)

# Slicing
text = "Python Programming"
print("\nOriginal string:", text)
print("Slicing [0:6]:", text[0:6])
print("Slicing [7:]:", text[7:])
print("Slicing [:6]:", text[:6])
print("Slicing [-11:]:", text[-11:])
print("Slicing [::2]:", text[::2])
print("Reverse string:", text[::-1])

# Length and indexing
print("\nLength:", len(text))
print("First character:", text[0])
print("Last character:", text[-1])
