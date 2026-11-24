student = {
    "name": "Bhavana",
    "age": 19,
    "course": "B.Tech",
    "city": "Vijayawada"
}

print("Original Dictionary:", student)

# keys()
print("Keys:", list(student.keys()))

# values()
print("Values:", list(student.values()))

# items()
print("Items:", list(student.items()))

# get()
print("Course using get():", student.get("course"))
print("Phone using get():", student.get("phone", "Not Found"))

# update()
student.update({"age": 20, "phone": "9876543210"})
print("After update():", student)

# pop()
removed_city = student.pop("city")
print("Removed city:", removed_city)
print("After pop():", student)

print("Final Dictionary:", student)
