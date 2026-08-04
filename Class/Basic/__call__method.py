
#Example 1
#The __call__ method permits you to create an object callable, rather than a function.
'''
Example 1: Basic Usage

Define the CallableObject class with the __call__ method that takes two arguments, x, and y, and returns their sum.
Create an instance of CallableObject named addition.
Call the addition instance with arguments 3 and 4. The __call__ method is invoked, and the result is the sum 7.
'''
class CallableObject:
    def __call__(self,x,y):
        return x+y

addition = CallableObject()
result = addition(3,4)
print(result)


# to make an instance of a class callable using __call__

#Here Without Assignment: args and kwargs are local variables scoped to the __call__ method.
class MyCallableClass:
    def __call__(self, *args, **kwargs):
        print(f"Called with arguments: {args} and keyword arguments: {kwargs}")

obj = MyCallableClass()
obj(1, 2, 3, a=4, b=5)
## Output: Called with arguments: (1, 2, 3) and keyword arguments: {'a': 4, 'b': 5}

#With Assignment: By assigning args and kwargs to self.args and self.kwargs, you make them accessible as attributes of the object.
class MyCallableClass:
    def __call__(self, *args, **kwargs):
        self.args = args  # Assign to self
        self.kwargs = kwargs  # Assign to self
        print(f"Called with arguments: {self.args} and keyword arguments: {self.kwargs}")

obj = MyCallableClass()
obj(1, 2, 3, a=4, b=5)


#example 2
class Calculation:
    def __init__(self,value):
        self.value=value
    def __call__(self,x):
        tsum=self.value+x
        tsub=self.value-x
        tmult=self.value*x
        tdiv=self.value/x
        return tsum,tsub,tmult,tdiv
        
# Create an instance of MyClass
obj = Calculation(10)

# Call the instance as if it were a function
result = obj.__call__(5)  # Equivalent to obj(5)
print(result)    # Output: 15,5,50,2.0

'''
"def __call__(self, *args: Any, **kwds: Any) -> Any:" where 

*args: Any, **kwds: Any: 
This part of the function signature defines two parameter lists:

*args is a tuple that collects any positional 
arguments passed to the function. 
The * symbol indicates that any number 
of positional arguments can be accepted.

**kwds is a dictionary that collects 
any keyword arguments passed to the function.
The ** symbol indicates that any number of 
keyword arguments can be accepted.

-> Any: This part of the function signature 
indicates the return type of the function. 
In this case, Any means that the function 
can return any type of data.

pass: This line is a placeholder statement 
that does nothing. It's often used when 
you want to define a function or method 
without implementing its behavior yet.

'''

#Example 3

class Polynomial:
   def __init__(self, coefficients):
      self.coefficients = coefficients
   
   def __call__(self, x):
      return sum(coefficient * x**power for power, coefficient in enumerate(self.coefficients))

quadratic = Polynomial([1, -2, 1])
result = quadratic(3) 
print(result)


'''
enumerate(self.coefficients):
        Iterates over the coefficients list, returning both the index (power) and the value (coefficient) for each element.
        For example, if coefficients = [1, -2, 1], enumerate(self.coefficients) produces:
            (0, 1) — coefficient is 1, power is 0
            (1, -2) — coefficient is -2, power is 1
            (2, 1) — coefficient is 1, power is 2

    x**power:
        Raises the value of x to the power of power.

    coefficient * x**power:
        Multiplies the coefficient by the result of raising x to the power.

    sum(...):
        Adds up all the terms in the polynomial.

Example: Evaluating quadratic(3)

The polynomial is represented by the coefficients [1, -2, 1], which corresponds to 1x2−2x+11x2−2x+1. Substituting x=3x=3:
1⋅32+(−2)⋅31+1⋅30
1⋅32+(−2)⋅31+1⋅30

    32=932=9, so 1⋅9=91⋅9=9
    31=331=3, so −2⋅3=−6−2⋅3=−6
    30=130=1, so 1⋅1=11⋅1=1

Adding these together:
9−6+1=4
9−6+1=4
'''










