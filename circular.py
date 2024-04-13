# Write a program that will convert degrees celsius to degrees fahrenheit.

import math
print("Enter the radius of the circle you would like the area and circumference of: ")
radius = float(input())
area = math.pi * (radius ** 2)
print("The area of the circle with radius, ", radius, " is ", area)
circumference = 2 * math.pi * radius
print("The circumference of the circle with radius, ", radius, " is ", circumference)