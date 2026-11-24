dict1 = {"name": "Bhavana", "age": 19}
dict2 = {"course": "B.Tech", "city": "Vijayawada"}

print("Dict 1:", dict1)
print("Dict 2:", dict2)

# Merge without changing original using copy() + update()
merged = dict1.copy()
merged.update(dict2)

print("Merged Dictionary:", merged)
print("Original Dict 1 (unchanged):", dict1)
print("Original Dict 2 (unchanged):", dict2)
