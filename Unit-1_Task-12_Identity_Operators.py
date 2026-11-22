# Demonstrate identity operators (is, is not)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a =", a)
print("b =", b)
print("c =", c)
print("a is b:", a is b)
print("a is c:", a is c)
print("a is not c:", a is not c)
print("b is not c:", b is not c)

x = 10
y = 10
print("x =", x)
print("y =", y)
print("x is y:", x is y)
print("x is not y:", x is not y)
