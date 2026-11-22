# Unit-2 Task 24: Reverse, Palindrome, Count, Frequency, Anagrams

text = input("Enter a string: ")

# 1. Reverse a string
reverse = text[::-1]
print("\nReversed String:", reverse)

# 2. Check Palindrome
if text.lower().replace(" ", "") == reverse.lower().replace(" ", ""):
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")

# 3. Count vowels, consonants, digits, spaces
vowels = consonants = digits = spaces = 0
for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print(f"\nVowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")

# 4. Frequency of each character
print("\nFrequency of each character:")
freq = {}
for ch in text:
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1

for k, v in freq.items():
    print(f"{k} : {v}")

# 5. Check Anagrams
print("\n--- Anagram Check ---")
s1 = input("Enter first string: ").lower().replace(" ", "")
s2 = input("Enter second string: ").lower().replace(" ", "")

if sorted(s1) == sorted(s2):
    print("They are Anagrams")
else:
    print("They are NOT Anagrams")