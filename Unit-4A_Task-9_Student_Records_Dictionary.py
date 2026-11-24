student = {
    "name": "Bhavana",
    "marks": 92,
    "grade": "A"
}

print("Student Record Dictionary:", student)

print("\nName:", student["name"])
print("Marks:", student["marks"])
print("Grade:", student["grade"])

print("\nFull Record:")
for key, value in student.items():
    print(key, ":", value)
