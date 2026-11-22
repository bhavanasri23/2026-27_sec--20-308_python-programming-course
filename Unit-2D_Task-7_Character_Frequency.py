# Count frequency of each character in a string

text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("String:", text)
print("Character Frequency:")
for ch, count in frequency.items():
    print(f"'{ch}' : {count}")
