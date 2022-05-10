from cgi import print_arguments
import imp


print("Ibrahim \n is good at playstation")

# This line will automatically add a new line before the 
# next print statement 
print("Ibarahim is the best person.")

# This print() function ends with "**" as set in the end argument.
print ("Ibrahim is the best person", end = " ** ")
print("Welcome Habibi")

import time 

count_seconds = 4
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end = '>>>')
    else: 
        print('Thats all ')

import time

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
	if i > 0:
		print(i, end='>>>', flush = True)
		time.sleep(1)
	else:
		print('Start')

b = "for"
print("Ibrahim" , b , "for one more time")

import io

# declare a dummy file
dummy_file = io.StringIO()

# add message to the dummy file
print('Hello Geeks!!', file=dummy_file)

# get the value from dummy file
dummy_file.getvalue()

# Python 3.x program showing
# how to print data on
# a screen

# One object is passed
print("GeeksForGeeks")

x = 5
# Two objects are passed
print("x =", x)

# code for disabling the softspace feature
print('G', 'F', 'G', sep='')

# using end argument
print("Python", end='@')
print("GeeksforGeeks")

