#This code is fine as long as you enter 10 not ten
num=int(input("Enter a number"))
print(num)
num += 10
print(num)

#Safest is to put code in a try accept block
try:
    num = int(input("Enter a number"))
    num += 10
except:
    print("You did not enter a number.")