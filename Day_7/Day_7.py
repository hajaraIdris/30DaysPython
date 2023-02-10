# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercises: Level 1
# 1 Find the length of the set it_companies
print(len(it_companies))
# 2 Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
# 3 Insert multiple IT companies at once to the set it_companies
more_it_companies ={'Whatapp','Tiktok','Telegram'}
it_companies.update(more_it_companies)
print(it_companies)
# 4 Remove one of the companies from the set it_companies
print(it_companies.pop())

# 5 What is the difference between remove and discard
''' remove() method: If the item is not found remove() method will raise errors, 
so it is good to check if the item exist in the given set. 
However, discard() method doesn't raise any errors.'''
it_companies.discard('Tiktok')
print('Tiktok' in it_companies) # discard

it_companies.remove('Telegram')
print('Telegram' in it_companies) # remove gave error

# Exercises: Level 2
# 1 Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#join_A_B
join_A_B = A.union(B)
print(join_A_B)
# 2 Find A intersection B
intersection_A_B = A.intersection(B)
print(intersection_A_B)

# 3 Is A subset of B
A_subset_B = A.issubset(B)
print(A_subset_B)
# 4 Are A and B disjoint sets
A_disjoint_B = A.isdisjoint(B)
print(A_disjoint_B)
# 5 Join A with B and B with A
join_A_B = A.union(B)
print(join_A_B)

join_B_A = B.union(A)
print(join_B_A)
# 6 What is the symmetric difference between A and B
symmetric_A_B = A.symmetric_difference(B)
print(symmetric_A_B)
# 7 Delete the sets completely
del A
del B

#Exercises: Level 3
# 1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set =set(age)
print(age_set)
age_len_lt=len(age)
print(' list_length :', age_len_lt)
age_len_set =len(age_set)
print(' set_length :', age_len_set)
print(age_len_lt> age_len_set)
# 2 Explain the difference between the following data types: string, list, tuple and set
age_string = str(age)
print("Str: %s" %(age_string))

age_list = age # is already a list
print("list: {}" .format(age_list))

age_tuple = tuple(age) 
print("tuple: {}" .format(age_tuple))

age_set = set(age) 
print("set: {}" .format(age_set)) # set sort and also remove duplicate
# 3 I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
str_data ='I am a teacher and I love to inspire and teach people.'
split_data =str_data.split( )
print(split_data)
unique_word =set(split_data)
print(unique_word)
print('Length :',len(unique_word))