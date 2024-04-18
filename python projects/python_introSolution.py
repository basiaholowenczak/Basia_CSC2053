print("hello world!")
# fast easy comment
'alternative to comment above'
'''
use this for longer block of comments
it can easily comment several lines
'''

# Variables
'''
Drawn on board 
int x = 100 (Java, must declare data type)
x = 100
can put any value in a variable
the value determines the data type
'''
x=100
y=5.5
x='hello'
x=[1,2,3]

# Math operations
# result is always a float
intx=100
inty=10
result=intx/inty
print(result)
# cast result to int
result=int(result)
print(result)

# an alternative is floor division which will discard any remainder
result = intx // inty
print(result)

# math module built in functions
min_val= min(10, 1)
print(min_val)
raised=pow(2,4)
print(raised)
# faster way
raised = 2**4
print(raised)

'''
main takeaways from lesson 1 are 
1. that variables are dynamic
2. if statements with conditional do not need to be wrapped in parenthesis and if statements need to end with a colon 
3. code is indented not in curly brackets
'''

# the full Python documentation including all built in functions can be found here:
# https://docs.python.org/3/library/index.html

# if statements and concatenating output
# blocks of code are not put in curly brackets 
# indentation is required
x = -1
y = 1
if x < 0:
    print('x is less than 0')
    x += 1

if x < 0 and y > 0:
    print('x and y within range')

if x < 0 or y < 0:
    print('x or y less than 0')

if x < 0:
    print('the value of x is', x, 'and it is less than 0')
elif x > 0:
    print('x is greater than 0')
else:
    print('x is 0')

# loops - for loop and while loop

#Default is that it starts at zero 
for i in range (5):
    print(i)

#Starts at 2 and goes through 5 so prints 2,3,4,5
for i in range (2,5):
    print(i)  

#Prints the length of the array 
nums = [10,20,30,40,50]
for i in range(len(nums)):
    print(nums(i))

#Prints values stored in nums array 
for num in nums:
    print(num)

#THIS DOESN"T WORK because it doesn't change value in original variable
for num in nums:
    num +=5
    print(num)
print(nums)

#This one does work
for i, val in enumerate(nums):
    print("1 is", i, "and val is", val)

#Use each loop type and iterate through the list of strings
    #creating an array of dogs 
dogs = ["boomer", "rocky", "daisy"]
#1
for i in range(len(dogs)):
    print(dogs(i))
#2
for num in dogs:
    print(dogs)
#3
for i, val in enumerate(dogs):
    print("1 is", i, "and val is", val)

#Create a list of numbers and use and loop to sum the numbers
nums = [1,2,3,4,5]
sum_nums = 0
for num in nums:
    sum_nums += nums 
print("sum of nums is", sum_nums) #can concattente strings but not any other data type
print(f"the sum of nums is {sum_nums}") #start print statement with f and then use curly brackets to draw in variable

counter = 0
while counter < 10:
    print(counter)
    counter += 1

'''
for loops are traditionally used to iterate through a list of items
In Java and JavaScript they lool like for (int i=0;i<array.length;i++)
Python's for loop does not look like that. There are a few options for the 
for loop.
Here we loop through a range of values starting at 0.
'''
a_list=[10,20,30,40,50]
for i in range(5):
    print(i, a_list[i])

# you can also use the len function to loop through the length of the list
# here we print each item and change the default ending of a new line to a space
# the print function takes an optional parameter, end where we can define how we want
# to separate each item printed.
# items will be printed next to each other instead of on a new line
for i in range(len(a_list)):
    print(a_list[i], end=" ")
print()

# You can also iterate backwards
# first parameter is the start - end of list len(list) -1
# next is where to end the decrement at -1
# next is value to decrement by
for i in range(len(a_list)-1, -1, -1):
    print(a_list[i])

'''
The other option is to use the enumerate function
enumerate takes a list of items and returns the index place and value
and stores them in assigned variables. In this example, it stores the
index place in i and the value in val.
'''
for i, val in enumerate(a_list):
    print(i, val)

# the final most simple loop is like the for each loop in Java
# here each item of the list is assigned to value on each iteration
for value in a_list:
    print(value)

# define a function like this
def hello_world():
    print("Hello World")

#This calls a function: 
hello_world()

# functions with a parameter 
def hello(name):
    print("Hello",name)
hello("Bob")
hello() #gives you an error because you are not giving it a parameter value

# Python functions accept default parameters for cases when you don't give it a value
def hello1(name="Bob"):
    print("Hello",name)
    #will only use default is someone uses function without giving it a parameter

hello_world()
hello1('Alice')
hello("James")

# Strings are a list of characters
f_name='kathleen'
l_name="malone"
full_name=f_name + " " + l_name

#Error: print('She's a great dancer'')
#Works 
print("she's a great dancer")
print('he said "hi" to his friend')

# access characters in a String with an index place
first_char=full_name[0]

# Python has a short cut to access elements starting from the end of the list using negative index places
# This works with any list not just strings
last_letter = full_name[-1]
print(last_letter)
second_last = full_name[-2]
print(second_last)



# Slice a string or a list
# string[start_index:end_index-1]
first_two_chars = full_name[0:2]
print(first_two_chars)

last_two_chars = full_name[-2:]
print(last_two_chars)

f_name=full_name[:8]
l_name=full_name[9:]
print(f_name, l_name)

platform_computing = "platform computing"
platform = platform_computing[:8]
computing = platform_computing[9:]
print(platform, computing)

#Goal: swap values 8 and 4 in nums
nums = [0,3,8,5,4]
'''
Do not hard coding it in
nums[2] = 4
nums[4] = 2

This works... until you have to replace nums[4]
nums[2] = nums[4]
nums[4] = nums[2]

'''
nums[2] = temp
nums[2] = nums[4]
num[4] = temp
print(nums)




# Repetition operator, *, will create a string made up of multiple copies of another
python_repeat3 = "python" * 3
print(python_repeat3)

#prints out name 3 times
name_3 = fname * 3

#Comparing strings
magician = "Harry Houdini"
if magician == 'Harry Houdini':
    print("world's greatest magician")