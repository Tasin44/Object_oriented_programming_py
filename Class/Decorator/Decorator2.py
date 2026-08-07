#approach 1
def timer(get_factorial):
    def inner():
        print('Time start')
        get_factorial()
        print('Time End')
    return inner


def get_factorial():
    print('Factorial')

timer(get_factorial)()

# we can also do this part timer(get_factorial)() in detailed way
# obj = timer(get_factorial)
# obj()


#=================================================================================================
#approach2
def timer(get_factorial):
    def inner():
        print('Time start2')
        get_factorial()
        print('Time End2')
    return inner

#Apply timer decorator to get_factorial:
@timer
def get_factorial():
    print('Factorial2')

get_factorial()#if I use @ decorator, then we've to call the original function

'''
You’re not directly calling the original get_factorial(), 
but instead calling the decorated version (inner()), 
which calls the original function as part of its body.
'''

'''
decorator(timer) takes the get_factorial function as an argument.
It returns a new function (inner) that first prints a message, calls get_factorial() and then prints another message.
The @timer syntax is a shorthand for get_factorial = decorator(get_factorial).
'''


#=============================================================================================================

def wrapper(func):
    print("Before calling original")
    func()
    print("After calling original")
    return func

@wrapper
def original():
    print("This is the original")

original()

'''
Output:


Before calling original
This is the original
After calling original
This is the original

'''












