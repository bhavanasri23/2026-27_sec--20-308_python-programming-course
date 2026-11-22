# Unit-3 Task 33: Demonstrate local and global scope of variables

# Global variable - bayata define chesam, anni functions lo kanipisthundi
x = 10
print("Global x =", x)

# 1. Local Scope
def show_local():
    # Local variable - ee function lopale matrame untundi
    y = 20
    print("\nInside show_local():")
    print("Local y =", y)
    print("Global x inside function =", x)

show_local()

# print(y) chesthe error vasthundi - y local kabatti
# print(y)  # NameError: name 'y' is not defined

# 2. Global variable ni function lo modify cheyadam - global keyword lekunda
def modify_without_global():
    x = 100  # idhi kotha local variable avthundi, global x maradu
    print("\nInside modify_without_global(): x =", x)

modify_without_global()
print("After modify_without_global(), Global x =", x)

# 3. Global keyword tho modify cheyadam
def modify_with_global():
    global x
    x = 50
    print("\nInside modify_with_global(): x =", x)

modify_with_global()
print("After modify_with_global(), Global x =", x)