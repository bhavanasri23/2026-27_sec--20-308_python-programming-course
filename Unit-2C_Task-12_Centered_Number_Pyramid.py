# Centered pyramid pattern of numbers
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    # Spaces for centering
    for j in range(rows - i):
        print(" ", end=" ")
    # Increasing numbers: 1 to i
    for k in range(1, i + 1):
        print(k, end=" ")
    # Decreasing numbers: i-1 to 1
    for k in range(i - 1, 0, -1):
        print(k, end=" ")
    print()
