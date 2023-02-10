# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string_1 ='Thirty'
string_2='Days'
string_3='Of'
string_4='Python'
space=' '
concatenate_strings= string_1 +space+ string_2 + space + string_3+ space + string_4

print(concatenate_strings)


#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string_1 ='Coding'
string_2='For'
string_3='All'
space=' '
concatenate_strings= string_1 +space+ string_2 + space + string_3
print(concatenate_strings)
print('Coding'+ ' '+'For'+ ' ' +'All')

# 3. declare a variable named company and assign it to an initial value "Coding For All".
#Company= string_1 +space+ string_2 + space + string_3
Company="Coding For All"
# 4 Print the variable company using print().
print(Company)
# 5 Print the length of the company string using len() method and print().
print(len(Company))
# 6 Change all the characters to uppercase letters using upper() method.
print(Company.upper())
# 7 Change all the characters to lowercase letters using lower() method.
print(Company.lower())
# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(Company.capitalize())
print(Company.title())
print(Company.swapcase())
# 9 Cut(slice) out the first word of Coding For All string.
print(Company[1:])
# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(Company.index('Coding'))
print(Company.find('Coding'))

# 11Replace the word coding in the string 'Coding For All' to Python.

print(Company.replace('Coding','Python'))
# 12 Change Python for Everyone to Python for All using the replace method or other methods.
Change_Python='Python For Everyone'
print(Change_Python.replace('Everyone', 'All'))

# 13 Split the string 'Coding For All' using space as the separator (split()) .
split_string='Coding For All'
print(split_string.split())
# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
Split_App="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(Split_App.split(','))
# 15 What character is at index 0 in "Coding For All" string.
print(split_string[0])
#16 What is the last index of the string Coding For All
print(split_string[-1])
#17 # 15 What character is at index 10 in "Coding For All" string.
print(split_string[10])
#18 Create an acronym or an abbreviation for the name 'Python For Everyone'
acronym=Change_Python[0],Change_Python[7], Change_Python[11]
print(''.join(acronym))
# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
acronym =split_string[0], split_string[7], split_string[11]
print(''.join(acronym))
# 20 Use index to determine the position of the first occurrence of C in Coding For All.
print(split_string.find('C'))
# 21 Use index to determine the position of the first occurrence of F in Coding For All.
print(split_string.find('F'))
#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(split_string.rfind('l'))

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

String_find= 'You cannot end a sentence with because because because is a conjunction'
print(String_find.find('because'))
# 24 use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(String_find.rfind('because'))
print(len(String_find))

#25 Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction
print(String_find[31:54])
#26 Find the position of the first occurrence of the word 'because' in the following sentence: 
#You cannot end a sentence with because because because is a conjunction'
print(String_find.find('because'))
#27 Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction
print(String_find[31:54])
#28 Does ''Coding For All' start with a substring Coding?
substring='Coding For All'
print(substring.startswith('Coding'))
# 29 Does 'Coding For All' end with a substring coding?
print(substring.endswith('coding'))
# 30'   Coding For All      '  , remove the left and right trailing spaces in the given string.
substring= '   Coding For All     '
print(substring.strip(' '))
#31 Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
substring='30DaysOfPython'
print(substring.isidentifier())
substring='thirty_days_of_python'
print(substring.isidentifier())
#32 The following list contains the names of some of python libraries: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string
list_libraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(list_libraries))

#33 Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.
print("I am enjoying this challenge.\n I just wonder what is next")

# 34Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
print('Name\t Age\t Country\t City')
print('Asabneh\t 250\t Finland\t Helsinki')

# 35 Use the string formatting method to display the following:
#radius = 10
#area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.
radius=10
area= 3.14 * radius **2
print('The area of a circle with radius 10 is {} meters square'.format(area))

# 36 Make the following using string formatting methods:
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144
print(' 8 + 6 ={}'.format(8+6))
print(' 8 - 6 =%d'%(8-6))
print(' 8 * 6 =%s'%(8*6))
print(' 8 / 6 =%.2f'%(8/6))
print(' 8 % 6 ={}'.format(8%6))
print(' 8 // 6 =%.2f'%(8/6))
print(' 8 ** 6 ={}'.format(8%6))