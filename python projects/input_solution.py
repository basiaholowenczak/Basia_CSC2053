'''
# input() will read in string
'''
# it can also display a prompt if given one
num=input("Enter a number")
print(num)

#This code is fine as long as you enter 10 not ten
num=int(input("Enter a number"))
print(num)
num += 10
print(num)

#Safest is to put code in a try accept block
# if user does not enter a number an exception will be thrown. 
try:
    num = int(input("Enter a number"))
    num += 10
except:
    print("You did not enter a number.")
print("Continue")

'''
# Different ways to use print
'''
name = "Jane"
greeting = "How are you?"
#1. Using a comma to output each string separated by a space - more convenient 
print("Hello", name, greeting)
#2. Using + to concatenate
print("Hello " + name + " " + greeting)
#3. Embed variables and expressions in f-string
print(f"Hello {name}! {greeting}")
age = 14
#This shows how you can embed expressions not just variables in print statements
print(f"{name} can vote in {18-age} years")
# use the end paramater to change what is printed after each statement
# a new line is the default
lst = [1,2,3,4,5]
for val in lst:
    print(val, end = " ")


'''
Open file and store each line in a list called file
Make sure that file is in the main 'CSC2053 folder' not in the 'python projects' folder
'''

#In this specific file, the last one is blank so when printing it out it shows an extra line... hence the need to do the 2nd version by stripping off the end line instead of the first version
with open("movies.txt") as file:
    for line in file:
        print(line)
with open("movies.txt") as file:
    for line in file:
        print(line.strip()) # strip off the end line

#.split returns a list where each word in string is a separate item in a list
with open("heights.txt") as file:
    for line in file:
        line=line.strip() # strip off end of line
        tokens = line.split() #split each word separated by a space and store in the list tokens
        print(tokens)
        print(tokens[0], ' ', tokens[1], 'is', tokens[2], 'inches tall.')

with open("heights.txt", 'r') as file:
        for line in file:
            data = line.strip().split()
            name = ' '.join(data[:-1])
            height = int(data[-1])
            heights_dict[name] = height

    return heights_dict