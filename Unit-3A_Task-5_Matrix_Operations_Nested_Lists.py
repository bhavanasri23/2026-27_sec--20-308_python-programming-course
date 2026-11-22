matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

print("Matrix 1:", matrix1)
print("Matrix 2:", matrix2)

# Addition
result = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("Addition of Matrices:", result)

# Transpose of Matrix 1
transpose = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        transpose[j][i] = matrix1[i][j]

print("Transpose of Matrix 1:", transpose)
