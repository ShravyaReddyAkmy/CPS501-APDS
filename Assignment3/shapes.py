# This program is to create a module called "shapes" 
# Written by: Shravya Reddy Akmy
# Date: 09/23/2021

# Python in-built library for mathemetical operations
import math   

# This method is used to calculate the parameters of geometric shape CIRCLE
# Input arguments : radius
# Output : Area, Circumference
def circle(radius):
    pi = round(math.pi) # Rounding the value of "pi(3.14)" to precision in decimals
    circle_area = radius*radius*pi 
    circle_circumference = 2*pi*radius
    return [circle_area,circle_circumference]

# This method is used to calculate the parameters of geometric shape SQUARE
# Input arguments : side
# Output : Area, Perimeter
def square(side):
    square_area = side*side
    square_perimeter = 4*side
    return [square_area,square_perimeter]

# This method is used to calculate the parameters of geometric shape RECTANGLE
# Input arguments : length,breadth
# Output : Area, Perimeter
def rectangle(length,breadth):
    rectangle_area = length*breadth
    rectangle_perimeter = 2*(length+breadth)
    return [rectangle_area,rectangle_perimeter]

# This method is used to calculate the parameters of geometric shape RHOMBUS
# Input arguments : diagonal1,diagonal2,side
# Output : Area, Perimeter
def rhombus(diagonal1,diagonal2,side):
    rhombus_area = (diagonal1*diagonal2)/2
    rhombus_perimeter = 4*side
    return [rhombus_area,rhombus_perimeter]




