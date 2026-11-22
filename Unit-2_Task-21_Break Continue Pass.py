# Unit-2 Task 21: Demonstrate break, continue and pass statements

print("--- break example ---")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("\n--- continue example ---")
for i in range(1, 10):
    if i == 5:
        continue
    print(i)

print("\n--- pass example ---")
for i in range(1, 6):
    if i == 3:
        pass
        print("pass chesam, emi cheyaledu")
    else:
        print(i)