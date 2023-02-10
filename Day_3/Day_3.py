
# 1: declare your age as interger
age=13
# 2: declare your height as float variable
height=5.4
#Declare a variable that store a complex number
complex_number=2+8j

# 4script that prompts user to enter base and height
# calculate the area of a triangle (area=0.5*b*h)
base=float(input('Enter base:'))
height=float(input('Enter height:'))
Area= 0.5*base*height
print(f'The area of the triangle is {Area}')

# 5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).

a=input('Enter side a:')
b=input('Enter side b:')
c=input('Enter side c:')
perimeter=a+b+c
print(f'The perimeter of the triangle is {perimeter}')

# 6 Get length and width of a rectangle using prompt. 
length=int(input('Enter Length of a triangle:'))
width=int(input('Enter width of a triangle:'))

Area_of_triangle = length * width       # Calculate its area (area = length x width) 
perimeter_of_triangle= 2 * (length + width) # perimeter (perimeter = 2 x (length + width)
print(f'the Area of the triangle is {Area_of_triangle} , and the perimeter is , {perimeter_of_triangle}')

#7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and 
# circumference (c = 2 x pi x r) where pi = 3.14.
radius_circle=int(input('Enter radius of a circle:'))
pi=3.142
Area  = pi * radius_circle * radius_circle
circumference =2*pi*radius_circle
print(f'the Area of the circle is {Area} , and the circumference is , {circumference}')

# 8 Calculate the slope, x-intercept and y-intercept of y = 2x -2

coefficient_x=2
print(coefficient_x)

# 9Slope is (m = y2-y1/x2-x1). 
# Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
x1,y1=2,2
x2,y2=6,10
slope = (y2-y1)/(x2-x1)

Euclidean_distance= math.sqrt((x2-x1)^2 +(y2-y1)^2) 
print(f"slope {slope}  Euclidean_distance: {Euclidean_distance}" )
# 10 Compare the slopes in tasks 8 and 9

print( coefficient_x == slope)
# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different 
# x values and figure out at what x value y is going to be 0
x=2
y =x^2 + 6*x+9  # y=21
print(f"x, y: {x} {y}")

x=2
y =(x**2) + (6 * x) + 9  # y=
print(f"x, y: {x} {y}")

x=-6
y =(x**2) + (6 * x) + 9  # y=2
print(f"x, y: {x} {y}")

x=-5
y =(x**2) + (6 * x) + 9  #y=4
print(f"x, y: {x} {y}")

x=-2
y =(x**2) + (6 * x) + 9  # y=4
print(f"x, y: {x} {y}")

x=-3
y =(x**2) + (6 * x) + 9  # y=0
print(f"x, y: {x} {y}")

#12  length of 'python' and 'dragon'
# and make a falsy comparison statement.
print(len('python') > len('dragon'))
#13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in ('python' and 'dragon'))

#14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print('jargon' in 'I hope this course is not full of jargon')
# There is no 'on' in both dragon and python
print('on' not in ('python' and 'dragon'))

# 16 Find the length of the text python and convert the value to float and convert it to string
print(float(len('python')))
print(str(len('python')))

# 17 Even numbers are divisible by 2 and the remainder is zero.
# How do you check if a number is even or not using python?
print(10%2 is 0 )

# 18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print(7//3 == int(2.7))
# 19Check if type of '10' is equal to type of 10
print( type('10') == (type(10)))

# 20 Check if int('9.8') is equal to 10
print((int(9.8)== 10))

# 21 Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
#Enter hours: 40
#Enter rate per hour: 28
#Your weekly earning is 1120
hours=float(input('Enter hours:'))
rate_per_hour=float(input('Enter rate per hour:'))
print("Your weekly earning is ", hours*rate_per_hour)

# 22 Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. Assume a person can live hundred years
#Enter number of years you have lived: 100
#You have lived for 3153600000 seconds.
number_of_years=float(input('Enter number of years you have lived:'))
print('You have lived for ', (number_of_years*365*24*60*60))


# 23 Write a Python script that displays the following table
#1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125
print("1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
