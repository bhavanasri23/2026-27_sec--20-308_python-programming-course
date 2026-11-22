# Reverse a string

text = input("Enter a string: ")

# Method 1: Using slicing
reversed_text = text[::-1]

print("Original string:", text)
print("Reversed string:", reversed_text)

# Method 2: Using loop (without slicing)
rev = ""
for ch in text:
    rev = ch + rev
print("Reversed string (using loop):", rev)
