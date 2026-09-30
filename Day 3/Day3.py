''' 
Day 3 of 30 Days of Python 
Initially completed on 9/1/26
Being redone to add to Github (and to fix some mistakes)
'''
# 1.1
age = 125
# 1.2
height = 6.5
# 1.3
number = 2j

# 1.4
base = input("Enter base: ")
base = float(base)
height = input("Enter height: ")
height = float(height)

area = base*height*.5

print("The area of the triangle is", area)

# 1.5
side_a = input("Enter side a: ")
side_a = float(side_a)
side_b = input("Enter side b: ")
side_b = float(side_b)
side_c = input("Enter side c: ")
side_c = float(side_c)

perimeter = side_a+side_b+side_c

print("The perimeter of the triangle is:", perimeter)

# 1.6
length = input("Enter the length: ")
length = float(length)
width = input("Enter the width: ")
width = float(width)

rect_area = length*width
rect_perimeter = (length+width)*2

print("The area is",rect_area,"and the perimeter is", rect_perimeter)