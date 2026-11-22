# Calculate simple interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print("Principal:", principal)
print("Rate:", rate)
print("Time:", time)
print("Simple Interest:", simple_interest)
print("Total Amount:", total_amount)
