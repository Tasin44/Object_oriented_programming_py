'''
# Positional Arguments:
the arguments passed to a function or method 
based on their position or order in the function's parameter list.
example:greet function
'''
def greet(name,age):
    print(f"Hello,{name}! You are {age} years old.")

greet("Alice",30)

# keyword arguments are matched based on their names.example:greeting function

def greetings(name,age):
    print(f"Hello,{name}! You are {age} years old.")

greetings(name="Karim",age="23")
'''
Functions defined outside of classes
are standalone and can be called directly 
without needing to create an instance of a class. 
Here greet and greetings are called directly without any class and class instance 
'''

'''
The greet and greetings method works 
without using any __init__ method 
because it's not part of a class. 
In Python, you can define functions
outside of classes, and they don't 
require an __init__ method.

'''
