'''
Python Lambda Functions are anonymous functions means that the function is without a name. 
As we already know the def keyword is used to define a normal function in Python. 
Similarly, the lambda keyword is used to define an anonymous function in Python. 
Python Lambda Function Syntax
lambda allows defining a simple one-line function without the need for a formal def.
  
Syntax: lambda arguments : expression
    lambda: The keyword to define the function.
    arguments: A comma-separated list of input parameters (like in a regular function).
    expression: A single expression that is evaluated and returned.

                                                                  
When to Use lambda
    Use lambda when defining small, simple functions inline.
    Avoid lambda for complex logic or when readability is a concern, as regular def statements are clearer in such cases.
'''


#Returning a Completely Different Callable(decorator4.py of github)

def replace_with_constant(func):
    # Returns a new function that ignores the original and always returns a constant
    return lambda *args, **kwargs: 42


@replace_with_constant
def calculate_sum(a, b):
    return a + b


print(calculate_sum(3, 5))  # Output: 42


#Equivalent Code Using def

def replace_with_constant(func):
    # Return a new function that always returns 42
    def constant_function(*args, **kwargs):
        return 42
    return constant_function


