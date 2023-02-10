# Exercises: Level 1

# 1 Create an empty tuple
Empty_tuple =()
print(Empty_tuple)
# 2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
names_sisters =('Aisha','Maimuna','Jemila','Amina','Fatima')
names_brothers =('Yahaya','Bello','Sodiq','Ibrahim')
print(names_sisters)
print(names_brothers)
# 3 Join brothers and sisters tuples and assign it to siblings
siblings = names_sisters + names_brothers
print(siblings)

#How many siblings do you have?
len_siblings = len(siblings)
print(len_siblings)
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings_list =list(siblings)
siblings_list.append('father')
siblings_list.append('mother')
family_members=siblings_list
family_members =tuple(family_members)

print(family_members)

# or
father_mother=('father','mother')
family_members = father_mother + siblings
print(family_members)


#Exercises: Level 2
# 1 Unpack siblings and parents from family_members
family_members = ['Aisha', 'Maimuna', 'Jemila', 'Amina', 'Fatima', 'Yahaya', 'Bello', 'Sodiq', 'Ibrahim', 'father', 'mother']
first_sibling,second_sibling,third__sibling, *others_sibling, Man, Woman = family_members
print(first_sibling)
print(second_sibling)
print(third__sibling)
print(others_sibling)
print(Man)
print(Woman)


# 2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits =('Apple','Orange', 'Apple','Banana')
vegetables= ('Okro','Tomatoes','Cucumber') 
animal_products = ('Hen','Dog','Donkey','Horses')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt =list(food_stuff_tp)
print(food_stuff_lt)
# 4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item =food_stuff_lt[5]
print(middle_item)

middle_item =food_stuff_tp[5]
print(middle_item)
# 5 Slice out the first three items and the last three items from food_staff_lt list
first_three_items =food_stuff_lt[0:3]
print(first_three_items)
last_three_items =food_stuff_lt[-3:]
print(last_three_items)

# 6 Delete the food_staff_tp tuple completely

list_food_stuff =list(food_stuff_tp)
list_food_stuff.clear()
food_stuff_tp =tuple(list_food_stuff)

# 7Check if an item exists in tuple:
print('Hen' in food_stuff_tp)
#food_stuff_tp)
#Check if 'Estonia' is a nordic country



nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)

#Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)
