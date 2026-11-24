# Sample dictionary
student = {
    "name": "Bhavana",
    "age": 19,
    "course": "B.Tech",
    "city": "Vijayawada"
}

print("Original Dictionary:", student)

# 1. keys() - anni keys chupisthundi
print("Keys:", list(student.keys()))

# 2. values() - anni values chupisthundi
print("Values:", list(student.values()))

# 3. items() - key-value pairs chupisthundi
print("Items:", list(student.items()))

# 4. get() - key tho value thechukovatam
print("Course using get():", student.get("course"))
print("Phone using get() with default:", student.get("phone", "Not Found"))

# 5. update() - kotha values add / update cheyadam
student.update({"age": 20, "phone": "9876543210"})
print("After update():", student)

# 6. pop() - oka key ni remove cheyadam
removed_city = student.pop("city")
print("Removed city:", removed_city)
print("After pop():", student)

print("Final Dictionary:", student)
