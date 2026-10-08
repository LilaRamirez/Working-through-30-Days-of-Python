'''
Day 5 of 30 Days of Python
Start Date: 10/8/26
'''

# 1.1
empty_list = []
print(f"This is an empty list: {empty_list}")

# 1.2
fruits = ['apple','blueberry','orange','banana','kiwi']
print(f"This is a list with items: {fruits}")

# 1.3 
print(f"The length of that list is {len(fruits)} elements.")

# 1.4
print(f"The first element is {fruits[0]}, the middle is {fruits[2]}, and the last is {fruits[-1]}")

# 1.5
# A list for name, age, height, marital status, adress. These will all be fake.
mixed_data_types = ['Luna', 25, 6.5, 'Not Married','123 Sesame Street']
print(f'A list of mixed data types: {mixed_data_types}')

# 1.6
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

# 1.7
# I have been printing this already...
print(f"A list of it companies: {it_companies}")

# 1.8
print(f'There is {len(it_companies)} names in that list')

# 1.9
print(f"The first company is {it_companies[0]}, the middle is {it_companies[3]}, and last one is {it_companies[-1]}")

# 1.10
it_companies[1] = 'Mozilla'
print(f'Modified list: {it_companies}')

# 1.11
it_companies.append('Google')
print(f'Appending to a list: {it_companies}')

# 1.12
it_companies.insert(3,'Nvidia')
print(f"Inserting in the middle of a list {it_companies}")

