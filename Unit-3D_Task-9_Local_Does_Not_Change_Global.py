x = 10  # global variable

def my_function():
    x = 20  # local variable, same name
    print("Inside function, x =", x)

my_function()
print("Outside function, x =", x)
print("Global variable did not change!")
