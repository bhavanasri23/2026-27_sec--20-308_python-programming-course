# Pascal's triangle
rows = int(input("Enter number of rows: "))

for i in range(rows):
    # Spaces for centering
    for j in range(rows - i - 1):
        print(" ", end=" ")
    # Pascal's values using formula: C(i, k)
    num = 1
    for k in range(i + 1):
        print(num, end=" ")
        num = num * (i - k) // (k + 1)
    print()
