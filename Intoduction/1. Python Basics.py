# Python code for "Hello World"
# nothing else to type...see how simple is the syntax.

print("Hello World")	

# Python program to declare variables
myNumber = 3
print(myNumber)

myNumber2 = 4.5
print(myNumber2)

myNumber ="helloworld"
print(myNumber)

# Python program to illustrate a list

# creates a empty list
nums = []

# appending data in list
nums.append(21)
nums.append(40.5)
nums.append("Ibrahim")

print(nums)

# Python program to illustrate
# getting input from user
name = input("Enter your name: ")

# user entered the name 'harssh'
print("hello", name)

# Python3 program to get input from user

# accepting integer from the user
# the return type of input() function is string ,
# so we need to convert the input to integer
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

num3 = num1 * num2
print("Product is: ", num3)

# Python program to illustrate
# selection statement

num3 = 34
if(num3 > 12):
	print("Num3 is good")
elif(num3 > 35):
	print("Num2 is not gooooo....")
else:
	print("Num2 is great")

# Python program to illustrate
# functions
def hello():
	print("hello")
	print("hello again")
hello()

# calling function
hello()			

# Python program to illustrate
# function with main
def getInteger():
	result = int(input("Enter integer: "))
	return result

def Main():
	print("Started")

	# calling the getInteger function and
	# storing its returned value in the output variable
	output = getInteger()	
	print(output)

# now we are required to tell Python
# for 'Main' function existence
if __name__== "__main__":
	Main()

# Python program to illustrate
# a simple for loop

for step in range(5):	
	print(step)

# Python program to illustrate
# math module
import math

def Main45():
	num12 = -85

	# fabs is used to get the absolute
	# value of a decimal
	num12 = math.fabs(num12)
	print(num12)
	
if __name__ == "__main__":
	Main45()

