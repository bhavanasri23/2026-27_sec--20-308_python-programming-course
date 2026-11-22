def total_average(marks1, marks2, marks3):
    total = marks1 + marks2 + marks3
    average = total / 3
    return total, average

m1 = 85
m2 = 90
m3 = 78

total, average = total_average(m1, m2, m3)

print("Marks:", m1, m2, m3)
print("Total Marks:", total)
print("Average Marks:", average)
