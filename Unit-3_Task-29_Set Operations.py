# Unit-3 Task 29: Set creation, operations, membership and methods

# 1. Set Creation
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
print("Set s1:", s1)
print("Set s2:", s2)

# 2. Set Operations
print("\n--- Set Operations ---")
print("Union (s1 | s2):", s1 | s2)
print("Union using union():", s1.union(s2))

print("\nIntersection (s1 & s2):", s1 & s2)
print("Intersection using intersection():", s1.intersection(s2))

print("\nDifference (s1 - s2):", s1 - s2)
print("Difference (s2 - s1):", s2 - s1)
print("Difference using difference():", s1.difference(s2))

print("\nSymmetric Difference (s1 ^ s2):", s1 ^ s2)

# 3. Membership
print("\n--- Membership ---")
print("Is 20 in s1?", 20 in s1)
print("Is 100 in s1?", 100 in s1)
print("Is 100 not in s1?", 100 not in s1)

# 4. Methods - add, remove, discard
print("\n--- Methods ---")
s1.add(60)
print("After add(60):", s1)

s1.remove(10)
print("After remove(10):", s1)

s1.discard(20)
print("After discard(20):", s1)

# discard() - lekapoina error raadu
s1.discard(100)
print("After discard(100) - no error:", s1)

print("\nLength of s1:", len(s1))