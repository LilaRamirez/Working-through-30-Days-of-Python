''' 
Day 4 of 30 Days of Python
Initially completed on 9/21/26
Being redone to add to Github (and to fix some mistakes)
'''

# 1.1
conc_list = ["Thirty ", "Days ", "of ", "Python"]
print(conc_list[0]+conc_list[1]+conc_list[2]+conc_list[-1])

# 1.2
str_one = "Coding "
str_two = "For "
str_three = "All"

full_str = str_one + str_two + str_three
print(full_str)
# Two different ways of doing the same thing, pretty much

# 1.3
company = "Coding For All"
# 1.4
print(company)
# 1.5
print(len(company))
# 1.6
print(company.upper())
# 1.7
print(company.lower())
# 1.8
print(f"{company.capitalize()}; {company.title()}; {company.swapcase()}")

# 1.9
no_coding = company[7:]
print(no_coding)

# 1.10
search = "Coding"
print(f"Where does {company} contain the word 'coding?'\n{company.index(search)}")

# 1.11
print(company.replace('Coding', 'Python'))

# 1.12
snake = "Python For Everyone"
print(snake.replace('Everyone', "All"))

# 1.13
# Empty to use spaces as the separator as opposed to 14 where it uses the comma
print(company.split())

# 1.14
tech_co = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_co.split(","))

# 1.15
print(f"The character at index 0 is {company[0]}")

# 1.16
print(f"The character at the last index is {company[-1]}")

# 1.17
print(f"The character at index 10 is {company[10]}") #This should return blank as it is a space

# 1.18
# Index returns a numerical value; we can use this value to pull the string value instead which is what we want for the acronym
first = company.index('C')
c= company[first]

second = company.index('F')
f = company[second]

third = company.index('A')
a = company[third]
acro = c+f+a
print(f"'Coding For All' acronym: {acro}")

# 1.19
# Ignoring the bad variable names, this is the exact same as before.
uno = snake.index('P')
p = snake[uno]

dos = snake.index('F')
f = snake[dos]

tres = snake.index('E')
e = snake[tres]
print(f"'Python for Everyone' acronym: {p+f+e}")

# 1.20
print(f"C can first be found at position {company.index('C')}")
# 1.21
print(f"F can first be found at position {company.index('F')}")

# 1.22
more = "Coding For All People"
print(f"'i' can be found at position {more.rfind('i')}")
# This is case sensetive; a capital I will return a -1

