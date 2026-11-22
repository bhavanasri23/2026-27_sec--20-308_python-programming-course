# Unit-3 Task 26: Largest, Smallest, Sum, Average, Second Largest, Duplicates

my_list = [10, 20, 30, 20, 40, 10, 50]
print("Original List:", my_list)

# 1. Largest and Smallest
print("\nLargest:", max(my_list))
print("Smallest:", min(my_list))

# 2. Sum and Average
total = sum(my_list)
print("\nSum:", total)
print("Average:", total / len(my_list))

# 3. Second Largest
unique_list = list(set(my_list))
unique_list.sort()
print("\nSecond Largest:", unique_list[-2])

# 4. Remove Duplicates
no_duplicates = []
for item in my_list:
    if item not in no_duplicates:
        no_duplicates.append(item)

print("\nAfter Removing Duplicates:", no_duplicates)