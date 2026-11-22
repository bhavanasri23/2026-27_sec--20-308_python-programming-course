counter = 0  # global variable

def increment():
    global counter
    counter += 1
    print("Inside function, counter =", counter)

increment()
increment()
increment()

print("Outside function, counter =", counter)
