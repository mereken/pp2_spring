import math

degree = int(input('Enter the degree: '))

rad = (degree/180)*math.pi
x = round(rad, 6)
print(f'Degree {degree} in radian is {x}')