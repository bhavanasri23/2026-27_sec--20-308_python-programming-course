# Calculate compound interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

amount = principal * (1 + rate/100) ** time
compound_interest = amount - principal

print("Principal:", principal)
print("Rate:", rate)
print("Time:", time)
print("Amount:", round(amount, 2))
print("Compound Interest:", round(compound_interest, 2))
