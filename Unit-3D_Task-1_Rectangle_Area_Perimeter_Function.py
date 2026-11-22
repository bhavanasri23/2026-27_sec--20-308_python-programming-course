def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

length = 10
breadth = 5

area, perimeter = rectangle(length, breadth)

print("Length:", length)
print("Breadth:", breadth)
print("Area:", area)
print("Perimeter:", perimeter)
