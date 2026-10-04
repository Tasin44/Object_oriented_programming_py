
'''
2. Method Overloading (Not directly supported in Python) ❌
In languages like Java, you can do this:
'''

# add(int a, int b)
# add(int a, int b, int c)


'''
Same method name, different number of parameters.

Python does NOT allow this.
'''
class Math:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):   # Replaces the first add()
        return a + b + c

'''
The first add() is overwritten by the second one.

How Python achieves overloading

Use default arguments:
'''


class Math:
    def add(self, a, b, c=0):
        return a + b + c

m = Math()
print(m.add(2, 3))      # 5
print(m.add(2, 3, 4))   # 9

# Or use *args:

class Math:
    def add(self, *nums):
        return sum(nums)

m = Math()
print(m.add(2, 3))        # 5
print(m.add(2, 3, 4))     # 9
print(m.add(1, 2, 3, 4))  # 10


'''
Quick difference

Method Overriding	                              Method Overloading

Child class changes                               parent's method	Same method name with different parameters
Uses inheritance	                              Doesn't require inheritance
Supported in Python	                              Not directly supported in Python
Example: Dog.sound() overrides Animal.sound()	  Simulated using default arguments or *args
'''

'''
Why sum(*args) won't work?

sum syntax is sum(iterable, start=0).

Iterable means something we can loop over: list, tuple, set, dict (iterates over keys), string, etc.

If args = (2, 5):

sum(*args) → sum(2, 5)
Here, 2 is treated as the iterable, but int is not iterable → error.

sum(args) → sum((2, 5))
Here, (2, 5) is the iterable → 2 + 5 = 7.

The start value is added to the final sum.
For example: sum((2, 5), 10) → 10 + 2 + 5 = 17.
'''