marks = {
    "Maths": 90,
    "Python": 95,
    "English": 88,
    "Physics": 85,
    "Chemistry": 92
}

print("Subject-Marks Dictionary:", marks)

print("\nKeys:")
for subject in marks.keys():
    print(subject)

print("\nValues:")
for mark in marks.values():
    print(mark)

print("\nItems:")
for subject, mark in marks.items():
    print(subject, ":", mark)
