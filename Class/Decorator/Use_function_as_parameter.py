'''
Functions in python are objects so we can pass them as 
arguments to other functions. Functions that can accept
other functions as arguments are also called higher-order functions. 
In the example below, a function greet is created which takes a function as an argument.

First Class Objects:
In Python, functions are first class objects 
which means that functions in Python can be 
used or passed as arguments.
Properties of first class functions:
# A function is an instance of the Object type.
# You can store the function in a variable.
# You can pass the function as a parameter to another function.
# You can return the function from a function.
# You can store them in data structures such as hash tables, lists, …
'''
def shout(text):
    return text.upper()
def wisper(text):
    return text.lower()

def greetings(f):
   print(f("Hi,My name is TasIn"))

greetings(shout)
greetings(wisper)