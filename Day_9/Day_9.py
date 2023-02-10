#Exercises: Day 9
     #Exercises: Level 1
     
# 1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. Output:
#Enter your age: 30
#You are old enough to learn to drive.
#Output:
#Enter your age: 15
#You need 3 more years to learn to drive.

age=int(input('Enter your age:'))
if age >= 18:
    print('You are old enough to drive.')
else: print('You need {} more years to learn to drive.'.format(18-age))


#2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year 
# difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
#Enter your age: 30
#You are 5 years older than me.
my_age =45
your_age=int(input('Enter your age:'))

if my_age > your_age:
    age=my_age - your_age
    if age==1:
        print('I am  1 year older than you')
    else:
        print('I am {} years older than you'.format(age))
elif my_age < your_age:
    age=your_age -my_age
    if age==1:
        print('You are  1 year older than me')
    else:
        print('You are %d years older than me' %age)
else :
    print(" We are both age mates")
    
    
    
    
# 3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
num_one =int(input('Enter number one:'))
num_two =int(input('Enter number two:'))

if num_one > num_two:
    print('{} is greater than {} '.format(num_one, num_two))
elif num_one < num_two:
    print('{} is smaller than {} '.format(num_one, num_two))
else:
    print('{} is equal to {} '.format(num_one, num_two))
    
#  Exercises: Level 2

#Write a code which gives grade to students according to theirs scores:

#80-100, A
#70-89, B
#60-69, C
#50-59, D
#0-49, F

student_scores =int(input('Enter student scores :'))
if student_scores >= 80:
    print('A')
elif student_scores >=70:
    print('B')
elif student_scores >=60:
    print('C')
elif student_scores >=50:
    print('D')
else :
    print('F')
    
# 2 Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer

check_season = input('Enter Month of year :')
if check_season == 'September'or check_season == 'October' or check_season == 'November':
    print('The season is Autumn')
elif check_season == 'December'or check_season == 'January' or check_season == 'February':
    print('The season is Winter')
elif check_season == 'March'or check_season == 'April' or check_season == 'May':
    print('The season is Spring')
elif check_season == 'June'or check_season == 'July' or check_season == 'August':
    print('The season is Summer')
    


# 3 The following list contains some fruits:

#fruits = ['banana', 'orange', 'mango', 'lemon']
 #If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
 # If the fruit exists print('That fruit already exist in the list')
 
input_fruit= input('Enter a fruit:')
fruits = ['banana', 'orange', 'mango', 'lemon']
print(input_fruit in fruits)
if input_fruit in fruits :
    print('That fruit already exist in the list')
else:
    fruits.append(input_fruit)
    print('fruits added:',fruits)
    print(fruits) 


#Exercises: Level 3
# 4 Here we have a person dictionary. Feel free to modify it!

'''    person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
    
    Asabeneh Yetayeh lives in Finland. He is married.
    '''

person= {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#if person['skills'] :
 ##  print(middle)
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    middle =int(len(person['skills'])/2)
    print(person['skills'][middle])
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills'in person:
    if 'Python' in person['skills']:
        print(person['skills'])

# If a person skills has only JavaScript and React, 
# print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') 
# - for more accurate results more conditions can be nested!
if person['skills'] == ['JavaScript', 'React']:
    print('He is a front end developer')
elif person['skills']==['Node','Python','MongoDB']:
    print('He is a backend developer')
elif person['skills']==['React', 'Node', 'MongoDB']:
    print('He is a fullstack developer')
else:
    print('unknown title')

#If the person is married and if he lives in Finland, print the information in the following format:
 # Asabeneh Yetayeh lives in Finland. He is married.
if person['is_married']== True and person['country'] is 'Finland':
    print('Asabeneh Yetayeh lives in Finland. He is married.')
