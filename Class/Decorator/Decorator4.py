#Question: a function returns something or an argument is passed to the function

def hello_decorator(sum_two_numbers):
    def inner1(*args, **kwargs):
        
        print("before Execution")
        
        # getting the returned value
        returned_value = sum_two_numbers(*args, **kwargs)
        print("after Execution")
        
        # returning the value to the original frame
        return returned_value
        
    return inner1#Return the inner1 function from hello_decorator.


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b
'''
Apply the hello_decorator to sum_two_numbers using the @hello_decorator syntax. 
This is equivalent to writing sum_two_numbers = hello_decorator(sum_two_numbers).
The sum_two_numbers function is now wrapped by the inner1 
function defined inside hello_decorator.

'''
a, b = 1, 2

# getting the value through return of the function
#Call the decorated(wraped) sum_two_numbers function with a and b as arguments.
print("Sum =", sum_two_numbers(a, b))



#Output:
#before Execution
#Inside the function
#after Execution
Sum = 3
#======================================================================================================================================================

'''
approach -2
'''
#if try to do without @

def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b

sum_two_numbers=hello_decorator(sum_two_numbers)

res= sum_two_numbers(3,5)
print(res)

# output
# before Execution
# after Execution
# Inside the function

def hello_decorator(sum_two_numbers):
    def inner1(a, k):
        print("before Execution")
        

        
        # returning the value to the original frame
        return sum_two_numbers(a,k)
        
    return inner1#Return the inner1 function from hello_decorator.


def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


sum_two_numbers=hello_decorator(sum_two_numbers)

res= sum_two_numbers(3,5)
print(res)


'''
it is not possible or logical to return hello_decorator like this:
return hello_decorator
 
Control Flow Problem:

    When you use return hello_decorator inside the hello_decorator function, you are trying to return the hello_decorator function itself instead of the inner1 function. This disrupts the intended functionality of the decorator.
    A decorator must return the inner (or wrapper) function that wraps the original function, not itself.

What Actually Happens:

    If you include return hello_decorator after return inner1, Python will ignore it because the first return statement (return inner1) already exits the function.
    The second return statement will never be reached.
'''

'''
Usually: A decorator returns an inner function (wrapper) to modify or extend the behavior of the decorated function.
Not Always: It can also return the original function, a different callable, or even something unexpected (though this is rare and unconventional).
'''

# Example : Returning a Completely Different Callable

# A decorator can return a completely different function or object if required.

def replace_with_constant(func):
    # Returns a new function that ignores the original and always returns a constant
    return lambda *args, **kwargs: 42

@replace_with_constant
def calculate_sum(a, b):
    return a + b

print(calculate_sum(3, 5))  # Output: 42

#Here, the decorator replace_with_constant ignores the original function and replaces it with a new function that always returns 42.


