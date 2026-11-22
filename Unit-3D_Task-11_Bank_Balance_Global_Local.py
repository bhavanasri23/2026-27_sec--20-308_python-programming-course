balance = 1000  # global balance

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ₹{amount}. New Balance: ₹{balance}")

def show_fake_balance():
    balance = 0  # local balance, does not affect global
    print(f"Inside show_fake_balance, local balance = ₹{balance}")

print("Initial Balance: ₹", balance)
deposit(500)
show_fake_balance()
print("Final Real Balance (global): ₹", balance)
print("Local balance did not change the real account!")
