# Unit-3 Task 32: Demonstrate variable-length arguments (*args, **kwargs)

# 1. *args - enni values aina ivvochu, tuple la vasthayi
def add_all(*args):
    print("args =", args)
    print("Sum =", sum(args))

print("--- *args ---")
add_all(10, 20)
add_all(1, 2, 3, 4, 5)
add_all(10, 20, 30, 40)

# 2. **kwargs - key=value pairs ivvochu, dictionary la vasthayi
def student_details(**kwargs):
    print("\nkwargs =", kwargs)
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print("\n--- **kwargs ---")
student_details(name="Bhavana", age=20, course="B.Tech")
student_details(name="Siri", city="Vijayawada")

# 3. Normal + *args + **kwargs kalipi
def display(a, *args, **kwargs):
    print("\n--- Combined ---")
    print("Normal argument a =", a)
    print("args =", args)
    print("kwargs =", kwargs)

display(10, 20, 30, name="Bhavana", age=20)