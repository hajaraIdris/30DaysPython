# Exercises: Level 1
1. #Declare an empty list
Empty_list=[]
# 2 Declare a list with more than 5 items

More_item =['item','item1','item2','item3','item4','item5','item6']
#4 Find the length of your list
print(len(More_item))
# 4. Get the first item, the middle item and the last item of the list
print(More_item[0], More_item[3], More_item[-1])
#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=['Aisha',"12",'6.5','single','Marafa Estate']
#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
it_companies=['Facebook','Google', 'Microsoft','Apple', 'IBM', 'Oracle', 'Amazon']
# 7 Print the list using print()
print(mixed_data_types)
print( it_companies)


# 8  Print the number of companies in the list
print(len(it_companies))

# 9 Print the first, middle and last company
print( it_companies[0], it_companies[3],  it_companies[6])

# 10 Print the list after modifying one of the companies
it_companies[3]='Whatapp'
print(it_companies)
# 11 Add an IT company to it_companies
it_companies.append('Twitter')
print(it_companies)

# 12 Insert an IT company in the middle of the companies list
it_companies.insert(4,'Gmail')
print(it_companies)
# 13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2]=it_companies[2].upper()
print(it_companies)

# 14 Join the it_companies with a string '#;  '
result= '#; '.join(it_companies)
print(result)

# 15 Check if a certain company exists in the it_companies list.
check_companies_exist = 'Whatapp' in it_companies
print(check_companies_exist)

# 16 Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17 Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
# 18 Slice out the first 3 companies from the list
first_three_companies=it_companies[:3]
print(first_three_companies)

# 19 Slice out the last 3 companies from the list
last_three_companies=it_companies[-3:]
print(last_three_companies)
# 20 Slice out the middle IT company or companies from the list
middle_iT_companies= it_companies[4]
print(middle_iT_companies)

# 21 Remove the first IT company from the list
it_companies.remove('Whatapp')
print(it_companies)


# 22 Remove the middle IT company or companies from the list
it_companies.remove('IBM')
it_companies.remove('Google')
print(it_companies)

# 23 Remove the last IT company from the list

it_companies.remove('Amazon')
print(it_companies)

# 24 Remove all IT companies from the list
it_companies.clear()
print(it_companies)
# 25 Destroy the IT companies list
del it_companies

# 26 Join the following lists:
#front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join_list= front_end + back_end
print(join_list)

# 27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack.
#Then insert Python and SQL after Redux.
full_stack=join_list.copy()
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)


#Exercises: Level 2
# The following is a list of 10 students ages:
    #ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    
# Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age =ages[0]
print(min_age)
max_age=ages[-1]
print(max_age)
# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)
# Find the median age (one middle item or two middle items divided by two)
median_ages = (ages[5] + ages[6])/2
print(median_ages)

# Find the average age (sum of all items divided by their number )
average_age= sum(ages)/len(ages)
print(average_age)
# Find the range of the ages (max minus min)
range_ages = max_age -min_age
print(range_ages)

# Compare the value of (min - average) and (max - average), use abs() method
min_average= abs(min_age - average_age)
print(min_average)
max_average= abs(max_age - average_age)
print(min_average)
print(float(min_average) == float(max_average))


# Find the middle country(ies) in the countries list

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
print(len(countries))
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries.append('Kasan')
print(len(countries))
countries_first_half=countries[0:96]
countries_second_half=countries[96:]
print('first_half :', countries_first_half)
print('second_half :', countries_second_half)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'] 
CH, RU, US, *scandic = countries_list
print("First_countries :", CH)
print("Second_countries :", RU)

print("Third_countries :", US)
print("Others_countries :", scandic)





