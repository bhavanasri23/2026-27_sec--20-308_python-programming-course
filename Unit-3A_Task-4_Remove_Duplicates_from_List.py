my_list = [10, 20, 10, 30, 20, 40, 30, 50]
print("Original List:", my_list)

new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)

print("List after removing duplicates:", new_list)
