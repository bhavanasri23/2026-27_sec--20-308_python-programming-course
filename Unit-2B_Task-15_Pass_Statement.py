# 1. using for loop - pass does nothing, loop continues
print("For loop with pass:")
for i in range(1, 11):
    if i == 5:
        pass
    print(i)

# 2. using while loop
print("While loop with pass:")
i = 1
while i <= 10:
    if i == 5:
        pass
    print(i)
    i += 1
