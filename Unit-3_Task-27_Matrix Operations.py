# Unit-3 Task 27: Matrix operations using nested lists

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

# 1. Matrix Addition
print("\n--- Addition (A + B) ---")
add = [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]
for row in add:
    print(row)

# 2. Matrix Subtraction
print("\n--- Subtraction (A - B) ---")
sub = [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)]
for row in sub:
    print(row)

# 3. Matrix Multiplication
print("\n--- Multiplication (A * B) ---")
mul = [[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        for k in range(3):
            mul[i][j] += A[i][k] * B[k][j]
for row in mul:
    print(row)

# 4. Transpose of A
print("\n--- Transpose of A ---")
transpose = [[A[j][i] for j in range(3)] for i in range(3)]
for row in transpose:
    print(row)