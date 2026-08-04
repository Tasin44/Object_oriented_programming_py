'''
Special Symbols Used for passing arguments in Python:
*args (Non-Keyword Arguments)
**kwargs (Keyword Arguments)

*args:
*args is used to pass a variable number of non-keyword arguments to a function.
It allows you to handle more arguments than the number of formal parameters you initially defined.
'''
def example_function(*args):
    for i in args:
        print(i)

example_function(1, 2, 3)
example_function('a', 'b', 'c')
#*args collects all the positional arguments passed to the function into a tuple.
'''
output:
1
2
3
a
b
c
'''
'''
**kwargs:
    **kwargs is used to pass a variable number of keyword arguments to a function.
'''

def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(name="John", age=30)
example_function(city="New York", country="USA")
#**kwargs collects all the keyword arguments passed to the function into a dictionary.

'''
Combining *args and **kwargs:

You can use both *args and **kwargs in the same function definition 
to accept both positional and keyword arguments.
'''


def example_function(*args, **kwargs):
    print("Positional arguments:")
    for i in args:
        print(i)
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(1, 2, 3, name="John", age=30)

'''
*args captures positional arguments into a tuple.
**kwargs captures keyword arguments into a dictionary.
'''





