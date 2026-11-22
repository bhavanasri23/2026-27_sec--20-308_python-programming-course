# Unit-3 Task 28: Create and access a tuple and demonstrate tuple operations

# 1. Create and Access a tuple
t1 = (10, 20, 30, 40, 50)
t2 = (60, 70, 80)
print("Tuple t1:", t1)
print("Tuple t2:", t2)

print("\n--- Accessing Tuple ---")
print("First element:", t1[0])
print("Last element:", t1[-1])
print("Second element:", t1[1])

# 2. Concatenation
print("\n--- Concatenation ---")
t3 = t1 + t2
print("t1 + t2 =", t3)

# 3. Slicing
print("\n--- Slicing ---")
print("t1[1:4] =", t1[1:4])
print("t1[:3] =", t1[:3])
print("t1[::2] =", t1[::2])

# 4. Unpacking
print("\n--- Unpacking ---")
a, b, c, d, e = t1
print("a =", a, "b =", b, "c =", c, "d =", d, "e =", e)

# 5. Swapping Variables using tuple
print("\n--- Swapping Variables ---")
x = 10
y = 20
print("Before Swapping: x =", x, "y =", y)
x, y = y, x
print("After Swapping: x =", x, "y =", y)

# 6. max() and min()
print("\n--- max() and min() ---")
print("Max in t1:", max(t1))
print("Min in t1:", min(t1))
print("Length:", len(t1))