my_list = [1, 2, 2, 3, 4, 4, 5, 1, 6, 3]

print("Original List:", my_list)

# Remove duplicates using set
unique_list = list(set(my_list))

print("After Removing Duplicates:", unique_list)

# If you want sorted output
print("Sorted Unique List:", sorted(unique_list))
