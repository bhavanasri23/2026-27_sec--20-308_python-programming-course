tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# Concatenation
combined = tuple1 + tuple2
print("After Concatenation:", combined)

# Slicing
print("Slicing [1:4]:", combined[1:4])
print("Slicing [:3]:", combined[:3])
print("Slicing [3:]:", combined[3:])

# Unpacking
a, b, c, d, e, f = combined
print("After Unpacking:")
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("e =", e)
print("f =", f)
