my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Membership testing
print("Is 3 in set?", 3 in my_set)
print("Is 10 in set?", 10 in my_set)
print("Is 10 not in set?", 10 not in my_set)

# add() method
my_set.add(6)
print("After add(6):", my_set)

my_set.add(3)
print("After add(3) again (no duplicate):", my_set)

# remove() method
my_set.remove(2)
print("After remove(2):", my_set)

# discard() method - no error if element not present
my_set.discard(4)
print("After discard(4):", my_set)

my_set.discard(100)
print("After discard(100) - no error:", my_set)
