a = [10,20,30,40,50]

# In Python we can use methods directly on the list
# Methods similar to methods used on ArrayLists in Java can be
# used directly on a list in Python
# add and remove items to list
# append, remove(item), pop() and pop(index)
# sort, reverse

'''
adding and removing values to list
'''
# Add values 5,6,7 to the existing list "a"
a.append(5)
a.append(6)
a.append(7)
print(a)

# Remove a value in 2 ways (by value or index place)
a.remove(50) #removes the number 50
a.pop(2) #removes the number at index place 2
print(a)
a.pop()
print(a)

'''
Reversing and sorting the list 
'''
a.reverse() #reverses existing list, does not create new one
print(a)
a.sort() #sorts existing list in ascending order, does not create new one
print(a)
    #if you want to sort in descending order, sort then reverse

# slice lists just like strings - String[start_index:end_index]
a=a[1:] #if you want to remove the first elemet 
print(a)

'''
.index and .count
'''
# returns the index place of 20 (index 2)
index7 = a.index(20)
print(index7)

# adding 20 to the list 3 times and then using count to count the number of times 20 shows up 
a.append(20)
a.append(20)
a.append(20)
num20 = a.count(20) #this can be helpful for hw 2
print(num20)

'''
Copying a list 
'''
#Copying a list is helpful for debugging
#BUT DO NOT DO THIS WAY
copy_lst = a 
copy_lst[0] = 99
print(copy_lst)
print(a) #If we modify the coipied list, we modify the original too because they both point to the same memory address 

#To actually make a copy without modifying original (safer):
    #1. use .copy makes a copy
copy_lst = a.copy()
copy_lst[-1] = 99
print(copy_lst)
print(a)
    #2. use slicing
new_copy = lst[0:]

'''
Adding values to an empty list (using a for loop)
'''
empty=[] #creates an empty list
#Adds values to list by iterative though list 
for val in a:
   empty.append(val)
print(empty) 

#Adding values to a list without iterating through
empty=[] #reinitializes it as empty 
#empty[0] = 10 --- gets eror index out of range when trying to assign value to a list without elements 
empty=[] * 10 #gives you an empty list with 10 values 
empty[0] = 10 

# Can't access element in list without initializing it first
empty=[]
# can't do this, it will raise an error
# empty[5] = 10
# initialize empty with 10 zeros
empty = [0] * 10
empty[5] = 10
print(empty)

# Only add values between 20 and 40
# for i in range(len(a)):
for val in a:
    if val >= 20 and val <= 40:
        empty.append(val)
print(empty)

# This can be used with strings too
dog = 'dog'
dogs = dog * 3
print(dogs)

# Operator is most often used to initialize lists
zeros = [0] * 1000
print(zeros)

'''
List comprehensions and iterating through lists 
'''
#Using a for loop
squares=[]
for i in range(1, 10):
    squares.append(i * i)
print(squares)

#Better to do a list comprehension instead of a for loop because it is much faster and less code
squares_comp=[i * i for i in range(1,10)]
print(squares_comp)
#1. Using comprehension you can to iterate through an existing list or create a new one
#2. Add 5 to each value stored in list and then store that new list in plus_5 
plus_5 = [val + 5 for val in a]
print(plus_5)
#3. Can also use list comprehension to filter values 
small_vals = [val for val in a if val < 20]
print(small_vals)
#4. Comprehensions can also use a conditional like if animale=='dog'
animals = ['dog','cat','dog','turtle']
dogs=[animal for animal in animals if animal == 'dog']
print(dogs)

'''
# Sets - unorder list of items
'''
aset = {1,2,3}
print(aset)
# Sets are unordered so we can't access them with an index place
# notallowed = aset[2]

# Sets don't allow duplicates
dups = [1,2,3,1,2,3]
no_dups = set(dups)
print(no_dups)

'''
# Dictionaries
'''
#Similar to a hashmap in java (key/value pairs)
#1. look up values 
#2. count occurances (frequency count)
#3. store values 

#Key and value are separated with a colon and each entry is separated by a commma
fav_foods={'Kathleen': 'pizza', 
           'Steve': 'burger', 
           'John': 'steak', 
           'Michelle': 'pasta', 
           'Patrick': 'pizza'}
print(fav_foods)

#Find value using key 
kff=fav_foods['Kathleen']
print(kff)

# Iterate through a dictionary, printing for each value in there
for key in fav_foods:
    print(key,'favorite food is',fav_foods[key])

#Another way to do it
for key,value in fav_foods.items():
    print(key,'favorite food is',value)

# check if key Bob is in dictionary and if not, puts Bob in the dictionary with favorite foods 
if 'Bob' in fav_foods:
    print("Bob's favorite food is",fav_foods['Bob'])
else:
    fav_foods["Bob"] = 'donuts'
print(fav_foods) #bob now added to dictionary 
