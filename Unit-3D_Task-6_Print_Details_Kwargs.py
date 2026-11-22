def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# Function call as given in question
print_details(name="Krishna", age=26, city="Guntur")
