import math

num_sides = int(input("Enter number of sides: "))
side_length = float(input("Enter number length of side: "))

s = (num_sides*side_length**2)/(4*math.tan(3.14/num_sides))
x = math.floor(s)
print(f'Area of polygon is {x}')
