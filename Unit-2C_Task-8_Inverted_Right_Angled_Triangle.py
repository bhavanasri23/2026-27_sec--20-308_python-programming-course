# Inverted right-angled triangle pattern
rows = int(input("Enter number of rows: "))
symbol = input("Enter symbol to print (e.g. * or 0): ")

for i in range(rows, 0, -1):
    for j in range(i):
        print(symbol, end=" ")
    print()
