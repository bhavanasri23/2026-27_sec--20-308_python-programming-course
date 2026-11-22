# Demonstrate membership operators (in, not in)

my_list = [10, 20, 30, 40, 50]
my_string = "Python Programming"

print("List:", my_list)
print("String:", my_string)
print("20 in my_list:", 20 in my_list)
print("60 in my_list:", 60 in my_list)
print("60 not in my_list:", 60 not in my_list)
print("20 not in my_list:", 20 not in my_list)
print("'Python' in my_string:", "Python" in my_string)
print("'Java' in my_string:", "Java" in my_string)
print("'Java' not in my_string:", "Java" not in my_string)

x = int(input("Enter a number to check in list: "))
print(x, "in my_list:", x in my_list)
print(x, "not in my_list:", x not in my_list)
