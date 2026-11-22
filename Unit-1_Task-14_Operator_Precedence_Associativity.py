# Demonstrate operator precedence and associativity

print("Precedence Examples:")
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)
print("10 - 4 + 3 =", 10 - 4 + 3)
print("2 * 3 ** 2 =", 2 * 3 ** 2)
print("10 / 2 * 3 =", 10 / 2 * 3)
print("10 + 20 / 2 =", 10 + 20 / 2)

print("\nAssociativity Examples (Left to Right):")
print("100 / 10 / 2 =", 100 / 10 / 2)
print("(100 / 10) / 2 =", (100 / 10) / 2)
print("100 - 20 - 10 =", 100 - 20 - 10)

print("\nAssociativity Examples (Right to Left):")
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)
print("2 ** (3 ** 2) =", 2 ** (3 ** 2))
print("(2 ** 3) ** 2 =", (2 ** 3) ** 2)
