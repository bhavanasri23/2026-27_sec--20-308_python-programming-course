students = {
    "Bhavana": {"Maths": 90, "Python": 95, "English": 88},
    "Siri": {"Maths": 85, "Python": 92, "English": 80},
    "Anu": {"Maths": 78, "Python": 89, "English": 91}
}

print("Students Nested Dictionary:", students)

for name, marks in students.items():
    print("\nName:", name)
    print("Marks:", marks)
    for subject, mark in marks.items():
        print(subject, ":", mark)
