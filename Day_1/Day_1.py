
# Day 1:Exercise
# 1 check the python version
import sys
print(sys.version)

# 2 operands 3 and 4 operations
print(3 + 4)       # addition(+)
print(3 - 4)      # subtraction(-)
print(3 * 4)      # multiplication(*)
print(3 % 4)      # modulus(%)
print(3 / 4)      # division(/)
print(3 ** 4)     # exponential(**)
print(3 // 4)     # Floor division operator(//)

# 3 String
print (' Hajara')      # my name
print (' Idris')       # my family name
print ('Nigeria')     # my country
print('I am enjoying 30 days of python')


# 4 check data type
print(type(10))                                     # int
print(type(9.8))                                    # float
print(type(3.14))                                   # float
print(type(4-4j))                                   # complex
print(type(['Asabeneh', 'Python', 'Finland']))      # List
print(type('Hajara'))                               # String
print(type('Idris'))                                # String
print(type('Nigeria'))                              # String

# Exercise Level 3
    # 1
print(type(10+5))                                            #  int
print(type(10.6 + 3.40))                                     #  float
print(type(10-4j))                                           # complex
print(type('Hello Python World'))                            # string
print(type(True))                                            # boolean
print(type(False))                                           # boolean
print(type(['Apple','Orange','Mango']))                      # List
print(type(('Apple','Orange','Mango')))                      # tuple
print (type({4,5,6,7,8}))                                    # set
print(type({1:'integer',2:'float',3:'double',4:'string'}))   # dictionary

    # 2
    # Euclidian distance between (2, 3) and (10, 8)

import math
x1,y1= (2,3)
x2,y2=(10,8)
Euclidean_distance= math.sqrt(((x2-x1)^2 +(y2-y1)^2) )
print(f"the Euclidian distance between (2, 3) and (10, 8) is {Euclidean_distance}" )

# end of the day exercise