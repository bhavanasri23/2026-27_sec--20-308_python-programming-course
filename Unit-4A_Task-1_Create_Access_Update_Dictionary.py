student = {
    "name": "Bhavana",
    "age": 19,
    "course": "B.Tech"
}

print("Original Dictionary:", student)
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

student["age"] = 20
print("After updating age:", student)

student["city"] = "Vijayawada"
print("After adding city:", student)
print("Final Dictionary:", student)
