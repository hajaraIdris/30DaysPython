# Write a python comment saying 'Day 2: 30 Days of python programming'
# Day 2 Exercise: 30 Days of python programming
# 3 declare a first name variable and assign a value to it
first_name= 'Aisha'
#Declare a last name variable and assign a value to it
last_name= 'Ibrahim'
#Declare a full name variable and assign a value to it
full_name= 'Aisha Ibrahim'
# Declare a country variable and assign a value to it
country='Nigeria'
# Declare a city variable and assign a value to it
city='Kaduna'
# Declare an age variable and assign a value to it
age=12
# Declare a year variable and assign a value to it
year=2002
# Declare a variable is_married and assign a value to it
is_married=False
#Declare a variable is_true and assign a value to it
is_true='yes'
#Declare a variable is_light_on and assign a value to it
is_light_on ='Yes'
#Declare multiple variable on one line
gender,programme,school='girl','computer_programming','IT'

# Exercise level 2
#1 Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(gender))

# 2 Using the len() built-in function, find the length of your first name
print(len(first_name))
# 3 Compare the length of your first name and your last name
print(first_name==last_name)

# 4 Declare 5 as num_one and 4 as num_two
num_one=5
num_two=4
#Add num_one and num_two and assign the value to a variable total
#Subtract num_two from num_one and assign the value to a variable diff
#Multiply num_two and num_one and assign the value to a variable product
#Divide num_one by num_two and assign the value to a variable division
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
#Calculate num_one to the power of num_two and assign the value to a variable exp
#ind floor division of num_one by num_two and assign the value to a variable floor_division

total=num_one+num_two
diff= num_two -num_one
product=num_two*num_one
division=num_one/num_two
remainder=num_two % num_one
exp = num_one^num_two
floor_division=num_one // num_two

# 5 The radius of a circle is 30 meters.
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#Take radius as user input and calculate the area.
pi=3.142
radius_circle= 30 #radius- 30meters
area_of_circle= pi * radius_circle**2
circum_of_circle = 2*pi*radius_circle
print(area_of_circle)
print(circum_of_circle)
radius=input('Enter the radius value: ')
Area=pi*radius_circle**2
print(Area)


# 6 Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name =input('Enter you first name:')
last_name=input('Enter your last name :')
country=input('what country are you from:')
age=input('how old are you: ?')
# 7 Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')