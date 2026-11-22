# Unit-3 Task 25: Create and traverse a list and perform list operations

# 1. Create a list
my_list = [10, 30, 20, 50, 40]
print("Original List:", my_list)

# 2. Traverse a list
print("\n--- Traverse List ---")
for item in my_list:
    print(item)

# 3. append() - chivarlo add cheyadam
my_list.append(60)
print("\nAfter append(60):", my_list)

# 4. insert() - madhyalo add cheyadam
my_list.insert(1, 15)
print("After insert(1, 15):", my_list)

# 5. remove() - okka value ni delete cheyadam
my_list.remove(30)
print("After remove(30):", my_list)

# 6. sort() - chinna nundi pedda ki
my_list.sort()
print("After sort():", my_list)

# 7. reverse() - reverse cheyadam
my_list.reverse()
print("After reverse():", my_list)