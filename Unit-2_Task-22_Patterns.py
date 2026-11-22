# Unit-2 Task 22: Print Patterns

n = 5

print("1. Right-Angled Triangle")
for i in range(1, n+1):
    print("* " * i)

print("\n2. Inverted Triangle")
for i in range(n, 0, -1):
    print("* " * i)

print("\n3. Number Pyramid")
for i in range(1, n+1):
    print(" " * (n-i) + " ".join(str(x) for x in range(1, i+1)))

print("\n4. Diamond of Stars")
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "* " * i)

print("\n5. Floyd's Triangle")
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

print("\n6. Pascal's Triangle")
for i in range(n):
    print(" " * (n-i), end="")
    val = 1
    for j in range(i+1):
        print(val, end=" ")
        val = val * (i-j) // (j+1)
    print()