''' 
Day 2 of 30 Days of Python 
Initially completed on 9/16/26
Being redone to add to Github (and to fix some mistakes)
'''
# 1.3
first_name = 'Jane'
print(f"First Name:{first_name}")

# 1.4
last_name = 'Doe'
print(f"Last Name: {last_name}")

# 1.5
full_name = first_name + ' ' + last_name
print(f"Full Name: {full_name}")

# 1.6
country = 'U.S.A.'
print(f"Country: {country}")

# 1.7
city = 'Cody'
print(f"City: {city}")

# 1.8
age = 20
print(f"Age: {age}")

# 1.9
year = 1776
print(f"Year: {year}")

# 1.10
is_married = False
print(f"Married?: {is_married}")

# 1.11
is_true = True
print(f"Is true true? {is_true}")

# 1.12
is_light_on = True
print(f"Is the light on? {is_light_on}")

# 1.13
time, color, number = '6 PM', 'Purple', 32
print(f"The time is {time}, the color is {color}, and the number is {number}.")

# 2.1

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(is_true))
print(type(time))
print(type(color))
print(type(number))

# 2.2
print(f"Length of First name: {len(first_name)}")

# 2.3
print(f"Compares the first and last name and finds the length of the greater value.\n{max(len(first_name),(len(last_name)))}")

# 2.4
num_one = 5
num_two = 4

# 2.5
total = num_one+num_two

# 2.6
diff = num_two-num_one

# 2.7
product = num_one*num_two

# 2.8
division = num_one/num_two

# 2.9
remainder = num_two%num_one

# 2.10
exp = num_one**num_two

# 2.11
floor_division = num_one//num_two

print(total,diff,product,division,remainder,exp,floor_division)

# 2.12
radius = 30
pi = 3.14 
#I don't remember a lot of digits of pi... this is fine for the purposes of this exercise.
area = pi*radius**2
circumference = pi*radius*2
print(f"A circle has an area of 30. The area is {area} and the circumference is {circumference}.")

user_radius = input("Type a Radius: ")
user_radius = float(user_radius)
user_area = pi*user_radius**2
print(f'The area of your circle is: {user_area}')

# 2.13
user_first_name = input('What is your first name? ')
user_last_name = input('What is your last name? ')
user_country = input('What country are you from? ')
user_age = input('How old are you? ')
print(f"User Info:\nFirst name: {user_first_name}\nLast name: {user_last_name}\nCountry: {user_country}\nAge: {user_age}")

# Day two complete! 2/29/26