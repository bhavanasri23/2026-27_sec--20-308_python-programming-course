# Task 9: Logical, Membership and Identity Operators

a = True
b = False

print("--- Logical Operators ---")
print("a and b =", a and b)
print("a or b =", a or b)
print("not a =", not a)

print("--- Membership Operators ---")
my_list = [1, 2, 3, 4, 5]
print("3 in list =", 3 in my_list)
print("10 not in list =", 10 not in my_list)
print("'a' in 'Python' =", 'a' in 'Python')

print("--- Identity Operators ---")
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print("x is z =", x is z)
print("x is y =", x is y)
print("x is not y =", x is not y)
