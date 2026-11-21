x = 2
y = 4.60
z = -3

#              ************************************<<Functions>>************************************

# result = round(y)
# result = abs(z)
# result = pow(4, 3)
# result = max(x, y, z)
# result = min(x, y, z)
# print(result)

#              ************************************<<Math Library>>************************************

import math as m
# Constant Numbers
# print(m.pi)
# print(m.e)
# result = m.sqrt(4)
# result = m.ceil(8.1)
# result = m.floor(8.9)
# print(result)

# Small project

radios = float(input("Enter a the radios of a circle "))

circumference = m.pi * 2 * radios
area = m.pi * pow(radios, 2)
print(f"Your Circumference is {circumference}cm")
print(f"Your Area is {area}cm^2")
