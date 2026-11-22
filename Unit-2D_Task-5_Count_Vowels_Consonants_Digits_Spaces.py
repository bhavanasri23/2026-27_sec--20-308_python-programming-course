# Count vowels, consonants, digits and spaces in a string

text = input("Enter a string: ")

vowels = consonants = digits = spaces = 0

for ch in text:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("String:", text)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
