
'''
A decorator in Python is a special function that modifies or adds extra behavior to another function or method without changing its original code.


A decorator is a function that takes another function 
as an argument and returns a new function, 
usually adding some functionality to the original 
function without modifying its code directly.
'''

# Syntax:
@decorator_name
def my_function():
    pass


# It is equivalent to:
def my_function():
    pass

my_function = decorator_name(my_function)


'''
In Python OOP

Decorators are commonly used to change how methods behave.

@classmethod → receives the class (cls) instead of an object (self).
@staticmethod → behaves like a normal function inside the class; it receives neither self nor cls.
@property → lets you access a method like an attribute.
'''


'''
in this code, 
wrapper_function serves as a decorator that decorates
original_function by adding extra functionality to it.
'''

def wrapper_function(func):#step 2
    def inner_function():#step 3
        print("Before calling the function")
        func()  # Call the original function
        print("After calling the function")
    return inner_function#step 4

def original_function():
    print("This is the original function")

# Wrap the original function with the wrapper function
wrapped_function=wrapper_function(original_function)#step 1
#will try to use orgianl function name here, it'll be benifacial for me difficult decorator function
#original_function=wrapper_function(original_function)#step 1

'''
We wrap the original_function with the wrapper_function 
by assigning the result of wrapper_function(original_function) to wrapped_function.
'''
# Call the wrapped function
wrapped_function()#step 5
#It's a function, not a object of a class,so we can directly call it without any __call__ method

'''
print(wrapper_function(original_function)) 

If i want to print like 
(wrapper_function(original_function))
that means printing the result of
calling wrapper_function(original_function) directly.
However, wrapper_function(original_function) returns the inner_function, 
not the result of calling the inner_function. 
Therefore, when you print wrapper_function(original_function),
means you're printing the reference of the inner_function, 
not executing it.
'''
