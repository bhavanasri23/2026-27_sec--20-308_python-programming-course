# 1. using for loop - skip 5
print("For loop with continue:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# 2. using while loop - skip 5
print("While loop with continue:")
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
