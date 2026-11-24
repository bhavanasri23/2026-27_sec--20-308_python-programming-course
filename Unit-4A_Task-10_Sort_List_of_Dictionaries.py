students = [
    {"name": "Bhavana", "marks": 92},
    {"name": "Siri", "marks": 85},
    {"name": "Anu", "marks": 95},
    {"name": "Ram", "marks": 78}
]

print("Original List:")
for s in students:
    print(s)

# Ascending order
ascending = sorted(students, key=lambda x: x["marks"])
print("\nAscending Order (by marks):")
for s in ascending:
    print(s)

# Descending order
descending = sorted(students, key=lambda x: x["marks"], reverse=True)
print("\nDescending Order (by marks):")
for s in descending:
    print(s)
