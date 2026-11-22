# Check whether a string is a palindrome

text = input("Enter a string: ")

# Remove spaces and convert to lowercase for fair comparison
cleaned = text.replace(" ", "").lower()
reversed_text = cleaned[::-1]

print("Original string:", text)
print("Reversed string:", reversed_text)

if cleaned == reversed_text:
    print(f"'{text}' is a Palindrome")
else:
    print(f"'{text}' is NOT a Palindrome")
