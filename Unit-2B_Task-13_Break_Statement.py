# 1. using for loop
print("For loop with break:")
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# 2. using while loop
print("While loop with break:")
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
