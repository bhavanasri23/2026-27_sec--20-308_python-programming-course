def student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# Function call
student_details(name="Bhavana", Maths=90, Science=85, English=88)
