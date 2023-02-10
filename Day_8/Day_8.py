# Dictionary
# 1 Create an empty dictionary called dog
dic_dog ={}
print(type(dic_dog))
# 2 Add name, color, breed, legs, age to the dog dictionary
dic_dog ={'name':'Bingo','color':'white','legs': 'long', 'age': 4}
print(dic_dog)
# 3 Create a student dictionary and add first_name, last_name, gender, age, marital status, 
# skills, country, city and address as keys for the dictionary
student={ 'first_name':'Bello',
         'last_name': 'Ahmed',
         'gender' : 'Male',
         'age':240,
         'marital_status':'married',
         'skills':['Python','Java','C#','C++','Machine_Learning'],
         ' country':'Nigeria',
         'city':{ 'Street_name': 'Marafa',
                  'Street_code': 1234,
                  'Street zip':12},
         'address':{'home_address': 'Kasuwar',
                   'address_zip': 12
                   }
         
         
        }
print(student)
# 4 Get the length of the student dictionary
print(len(student))
# 5 Get the value of skills and check the data type, it should be a list
#skills =student.get('skills')
skills =student['skills']
print(skills)
print(type(skills))
 
# 6Modify the skills values by adding one or two skills
student['skills'][2] ='Cobol'           # modify
student['skills'][4] ='Visual basic'

student['skills'].append('JavaScripts')
student['skills'].append('PHP')


print(student)
# 7 Get the dictionary keys as a list
print("Keys :",student.keys())

# 8 Get the dictionary values as a list
print("Values :",student.values())
# 9 Change the dictionary to a list of tuples using items() method
tuple_student = student.items()

print('\n ',tuple_student)
# 10 Delete one of the items in the dictionary
student['city'].popitem()
print('\n',student['city'])
# 11 Delete one of the dictionaries
del student['gender']
print('gender' in student)