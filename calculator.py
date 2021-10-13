	#!/usr/bin/env python3
"""
	Define the arithmetic functions to return the result(s). Please
	do not rename the functions. You may create new functions for additional functionality, if required

"""

value=input("enter your chouce:\n")

input(a,b)

# Define your addition function here.
def add(a,b):
	# Your code goes here
	return(a+b)

# Define your subtraction function here.
def subtract(a,b):
	# Your code goes here
	return(a-b)
	pass

# Define your multiplication function here.
def multiply(a,b):
	# Your code goes here
	return(a*b)
	pass

# Define your division function here.
def divide(a,b):
	# Your code goes here
	return(a/b)
	pass

# Define your division function here.
def divide_integer(a,b):
	# Your code goes here
	return(a//b)
	pass

if __name__ == "__main__":
	print("*****"*5)
	print(" A SIMPLE CALCULATOR")
	print("*****"*5)
	# Your main code here

print("what action do you want to perform:\n"
    "add\n"
    "sub\n"
    "multi\n"
    "div\n"
    "intdiv")

value,a,b=input(),input(),input()

def choice(value):
    if(value=="add"):
        return(a+b)
    elif(value=="sub"):
        return(a-b)
    elif(value=="multi"):
        return(a*b)
    elif(value=="div"):
        return(a/b)
    else:
        return(a//b)