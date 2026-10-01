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
print("Triangle Area Calculator:")
base = input("Enter base: ")
base = float(base)
height = input("Enter height: ")
height = float(height)

area = base*height*.5

print("The area of the triangle is", area)

# 1.5
print('Triangle perimeter calculator:')
side_a = input("Enter side a: ")
side_a = float(side_a)
side_b = input("Enter side b: ")
side_b = float(side_b)
side_c = input("Enter side c: ")
side_c = float(side_c)

perimeter = side_a+side_b+side_c

print("The perimeter of the triangle is:", perimeter)

# 1.6
print("Rectangle area and perimeter calculator:")
length = input("Enter the length: ")
length = float(length)
width = input("Enter the width: ")
width = float(width)

rect_area = length*width
rect_perimeter = (length+width)*2

print("The area is",rect_area,"and the perimeter is", rect_perimeter)

# 1.7
PI = 3.14
print('Circle Area Calculator:')
radius = input("Enter a Radius: ")
circle_area = PI*float(radius)**2
print(f"The area of the circle is: {circle_area}")

# 1.8
x = 0
y_int = 2*x-2
x_int = 2 /2
slope_a = 2
# I'm not going to be importing anything so I mostly just did the math in my head.
print(f"Given the equation y = 2x - 2, find the y-intercept, x-intercept, and slope.\ny-int: {y_int,-2}\nx-int: {int(x_int),0}\nSlope: {slope_a}")

# 1.9
x1_minus_x2 = 10-2
y1_minus_y2= 6-2
slope_b = y1_minus_y2/x1_minus_x2
print(f"The slope of a line that intersects with (2,2) and (6,10) is {slope_b}.")

# 1.10
print("Are the previous slopes equal? ",bool({slope_a}=={slope_b}))

# 1.11
# A bit unsure of what the question is aksing to do here so I decided this was my solution.
# To get x intercept, type -3.

print('Solves for the equation x^2 + 6x - 9\n')
x = input('Insert a value for x here: ')
x = float(x)
solve = x**2 + 6*x + 9
print(f"When x is equal to {x}, y is equal to {solve}")

# 1.12
# Would this have been easier by not making a list? Perhaps.
animals = ["dragon","python"]
print("Are dragon and python the same lenght?",bool(len(animals[0])==len(animals[1])))

# 1.13
print('Is there "on" in both words?', bool('on' in animals[0] and animals[1]))

# 1.14
phrase = 'I hope this course is not full of jargon'
print("Is 'jargon' in the phrase?",bool('jargon' in phrase))

# 1.15
# This question doesn't really tell what it wants, so I decided to go with a not operator.
print("There is no 'on' in dragon and python:", not True)

# 1.16
word_length = len('Python')
print(f'The length of the word "Python" is {word_length}')
word_length = float(word_length)
print(f"Here's that value as a float! {word_length} {type(word_length)}")
word_length = str(word_length)
print(f"And here's that same value again as a string. {word_length}, {type(word_length)}")

# 1.17
print("The even calculator! Input a number to see if it's even or odd.")
number = input()
number = float(number)
number%=2
if number == 0.0:
    print('Your number is even!')
else:
    print('Your number is not even.')

# 1.18
floor_1 = 7//3
floor_2 = int(2.7)
print(f"Is 7//3 equal to the int value of 2.7? {floor_1==floor_2}")

# 1.19
# I think this is comparing two different types (string vs int)
print(f"Is '10' equal to 10? {'10'== 10}")

# 1.20
print(f"Is int('9.8') equal to 10? {int(9.8) == 10}")

# 1.21
print("Weekly earning calculator:")
hours = input("Enter hours (per week): ")
hours = float(hours)
money = input("Enter rate per hour: ")
money = float(money)
mpw = hours*money
print(f"Your weekly earning is {mpw}")

# 1.22
print("How long have you lived? (in seconds)")
years = input("Enter your age: ")
years = int(years)
total = years*31536000
print(f"You have lived for {total} seconds.")