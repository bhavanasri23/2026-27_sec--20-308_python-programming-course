def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si

# Call using default rate (5)
si1 = simple_interest(10000, 2)
print("Principal: 10000, Time: 2 years, Rate: 5% (default)")
print("Simple Interest:", si1)

# Call with explicit rate
si2 = simple_interest(10000, 2, 8)
print("Principal: 10000, Time: 2 years, Rate: 8% (explicit)")
print("Simple Interest:", si2)
