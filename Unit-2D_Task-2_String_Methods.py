# Demonstrate string methods: upper, lower, strip, split, join, replace, find

text = "  Hello Python Programming  "
print("Original string:", repr(text))

# upper() and lower()
print("\nupper():", text.upper())
print("lower():", text.lower())
print("title():", text.title())

# strip() - removes leading and trailing spaces
stripped = text.strip()
print("\nstrip():", repr(stripped))
print("lstrip():", repr(text.lstrip()))
print("rstrip():", repr(text.rstrip()))

# split() - splits string into list
words = stripped.split()
print("\nsplit():", words)
print("split('o'):", stripped.split('o'))

# join() - joins list into string
print("\njoin() with space:", " ".join(words))
print("join() with '-':", "-".join(words))

# replace() - replaces a part of string
print("\nreplace('Python', 'Java'):", stripped.replace("Python", "Java"))

# find() - returns index, -1 if not found
print("\nfind('Python'):", stripped.find("Python"))
print("find('Java'):", stripped.find("Java"))
print("find('o'):", stripped.find("o"))
print("count('o'):", stripped.count("o"))
